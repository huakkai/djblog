from django.db import models


class Tag(models.Model):
    name = models.CharField('Tag', max_length=100)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
