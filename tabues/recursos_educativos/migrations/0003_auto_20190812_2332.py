# Generated by Django 2.2.3 on 2019-08-13 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_educativos', '0002_auto_20190811_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educational_resource',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='educational_resource',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='recursos-educativos/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='learning',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='learning',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(upload_to='recursos-educativos/aprende', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='learning',
            name='thematic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recursos_educativos.Thematic', verbose_name='Temática'),
        ),
        migrations.AlterField(
            model_name='thematic',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Nombre'),
        ),
        migrations.CreateModel(
            name='EduFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=350)),
                ('archivo_pdf', models.FileField(upload_to='recursos-educativos/archivos/')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos_educativos.Educational_Resource', verbose_name='Archivo')),
            ],
            options={
                'verbose_name_plural': 'Archivos',
            },
        ),
    ]
