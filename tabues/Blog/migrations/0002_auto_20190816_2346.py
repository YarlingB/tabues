# Generated by Django 2.2.3 on 2019-08-17 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recursos_educativos', '0002_auto_20190816_2346'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Separe con "," cada elemento', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='blog',
            name='thematic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recursos_educativos.Thematic', verbose_name='Temática'),
        ),
        migrations.AddField(
            model_name='answer',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Comment', verbose_name='Comentario'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
