from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger

# Create your views here.
from blog.models.article import Article
from blog.models.category import Category


def index(request):
    post_list = Article.objects.all().order_by("-id")
    context = _get_context(request=request, post_list=post_list)
    return render(request, 'index.html', context)


def show(request, uid):
    article = Article.objects.get(uid=uid)
    article.views += 1
    article.save()
    category = Category.objects.all()
    context = {
        'site': settings.SITE,
        'article': article,
        'category': category,
        'author': settings.AUTHOR,
        'github': settings.GITHUB,
    }
    return render(request, 'show.html', context)


def about(request):
    context = {
        'site': settings.SITE,
        'author': settings.AUTHOR,
        'github': settings.GITHUB,
    }
    return render(request, 'about.html', context)


def category(request, category_id):
    post_list = Article.objects.filter(category=category_id).order_by("-id")
    context = _get_context(request=request, post_list=post_list)
    return render(request, 'index.html', context)


def search(request):
    q = request.GET.get('q')
    post_list = Article.objects.filter(title__contains=q).order_by("-id")
    context = _get_context(request=request, post_list=post_list)
    return render(request, 'index.html', context)


def _get_context(request=None, post_list=None):
    category = Category.objects.all()
    after_range_num = 3    # 当前页前显示 3 页
    before_range_num = 3   # 当前页后显示 3 页
    try:                   # 如果请求的页码少于 1 或者类型错误，则跳转到第 1 页
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(post_list, 10)
    count = paginator.count
    try:           # 跳转到请求页面，如果该页不存在或者超过则跳转到尾页
        post_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        post_list = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num: page + before_range_num]
    else:
        page_range = paginator.page_range[0: int(page) + before_range_num]
    context = {
        'site': settings.SITE,
        'category': category,
        'post_list': post_list,
        'page_range': page_range,
        'count': count,
        'author': settings.AUTHOR,
        'github': settings.GITHUB,
    }
    return context
