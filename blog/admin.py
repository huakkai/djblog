from django.contrib import admin
from .models.category import Category
from .models.tag import Tag
from .models.article import Article


admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)

# Register your models here.
