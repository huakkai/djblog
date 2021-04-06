from django.db import models


class Category(models.Model):
    STYLE_CHOICES=[
        ('badge-default', 'badge-default'),
        ('badge-primary', 'badge-primary'),
        ('badge-success', 'badge-success'),
        ('badge-info', 'badge-info'),
        ('badge-warning', 'badge-warning'),
        ('badge-danger', 'badge-danger'),
    ]
    name = models.CharField('Blog Category', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='badge-default', max_length=100, verbose_name='Style')
    index = models.IntegerField(default=1, verbose_name='Sequence')

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
