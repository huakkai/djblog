# Generated by Django 3.1.7 on 2021-04-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210320_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='style',
            field=models.CharField(choices=[('badge-default', 'badge-default'), ('badge-primary', 'badge-primary'), ('badge-success', 'badge-success'), ('badge-info', 'badge-info'), ('badge-warning', 'badge-warning'), ('badge-danger', 'badge-danger')], default='badge-default', max_length=100, verbose_name='Style'),
        ),
    ]
