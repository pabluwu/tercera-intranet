# Generated by Django 4.2.5 on 2024-01-23 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0018_alter_tipodocumento_slug_alter_tipodocumento_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='ruta',
            field=models.CharField(default='peo', max_length=500, unique=True),
            preserve_default=False,
        ),
    ]
