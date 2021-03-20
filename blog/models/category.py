from django.db import models


class Category(models.Model):
    name = models.CharField('Blog Category', max_length=100)
    index = models.IntegerField(default=1, verbose_name='Sequence')

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
