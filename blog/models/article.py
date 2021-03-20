import uuid as uuid
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from blog.models.tag import Tag
from blog.models.category import Category
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField('Title', max_length=70)
    summary = RichTextField('Summary', max_length=200, blank=True, config_name='editor_config')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Category', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tag', blank=True)
    img = models.ImageField(upload_to='media/img/%Y/%m/%d/', verbose_name='Image', blank=True, null=True)
    body = RichTextUploadingField(config_name='editor_config')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField('Views', default=0)
    created_time = models.DateTimeField('Create Date', auto_now_add=True)
    modified_time = models.DateTimeField('Update Date', auto_now=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Article'

    def __str__(self):
        return self.title
