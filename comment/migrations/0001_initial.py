# Generated by Django 4.2.1 on 2023-06-22 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0011_delete_comments'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='评论内容')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.articles', verbose_name='所属文章')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者')),
                ('parent', models.ForeignKey(blank=True, help_text='可以为空', null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.comments', verbose_name='父级评论')),
            ],
        ),
    ]
