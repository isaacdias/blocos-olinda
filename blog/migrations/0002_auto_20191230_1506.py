# Generated by Django 3.0.1 on 2019-12-30 18:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='imagem'),
        ),
    ]
