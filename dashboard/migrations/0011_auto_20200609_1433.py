# Generated by Django 2.2.6 on 2020-06-09 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20200430_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salle',
            old_name='type',
            new_name='type_of',
        ),
    ]