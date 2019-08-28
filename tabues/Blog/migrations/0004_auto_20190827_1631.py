# Generated by Django 2.2.3 on 2019-08-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_comment_is_anonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_anonymous',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_anonymous',
            field=models.BooleanField(),
        ),
    ]
