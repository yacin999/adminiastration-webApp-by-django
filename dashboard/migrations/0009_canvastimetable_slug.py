# Generated by Django 2.2.6 on 2020-04-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20200417_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvastimetable',
            name='slug',
            field=models.SlugField(default='licence', unique=True),
            preserve_default=False,
        ),
    ]
