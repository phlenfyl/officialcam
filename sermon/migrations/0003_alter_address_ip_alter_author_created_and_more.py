# Generated by Django 4.2.6 on 2023-11-29 13:05

import cloudinary.models
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('sermon', '0002_sermon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='ip',
            field=models.CharField(blank=True, default='0.0.0.0', max_length=40, null=True, unique=True, verbose_name='ip address'),
        ),
        migrations.AlterField(
            model_name='author',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='author',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio', verbose_name='audio'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='sermon', verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='like_count',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='like_count'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]
