# Generated by Django 2.2.6 on 2020-09-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0031_auto_20200919_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargehoraire',
            name='semestre',
            field=models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('M1', 'M1'), ('M2', 'M2')], max_length=20),
        ),
    ]
