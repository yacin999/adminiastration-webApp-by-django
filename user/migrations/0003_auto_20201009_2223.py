# Generated by Django 2.2.6 on 2020-10-09 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201001_0754'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='staffpermission',
            table='droit_acces',
        ),
    ]