# Generated by Django 4.2.5 on 2024-01-23 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0017_tipodocumento_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodocumento',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tipodocumento',
            name='tipo',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
