# Generated by Django 4.2.4 on 2023-08-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0003_citacion_lugar_citacion_tenida_alter_citacion_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citacion',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
    ]
