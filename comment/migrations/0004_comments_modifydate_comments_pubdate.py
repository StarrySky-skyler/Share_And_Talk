# Generated by Django 4.2.1 on 2023-06-22 18:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_alter_likes_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='modifyDate',
            field=models.DateTimeField(auto_now=True, verbose_name='修改日期'),
        ),
        migrations.AddField(
            model_name='comments',
            name='pubDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='发布日期'),
            preserve_default=False,
        ),
    ]
