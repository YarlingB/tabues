# Generated by Django 2.2.3 on 2019-08-12 04:09

import ckeditor_uploader.fields
from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to='')),
                ('about', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Descripción')),
                ('slug', models.SlugField(editable=False, max_length=200)),
            ],
        ),
    ]
