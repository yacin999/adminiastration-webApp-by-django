# Generated by Django 2.2.6 on 2020-10-14 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20201014_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='departement',
            field=models.CharField(choices=[('1', 'informatique'), ('2', 'mathématique')], default='informatique', max_length=30),
            preserve_default=False,
        ),
    ]
