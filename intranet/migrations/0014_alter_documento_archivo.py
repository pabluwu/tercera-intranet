# Generated by Django 4.2.5 on 2024-01-22 23:53

from django.db import migrations, models
import intranet.validators


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0013_documento_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='archivo',
            field=models.FileField(default='logos/logo.png', upload_to='docs/', validators=[intranet.validators.file_size]),
        ),
    ]
