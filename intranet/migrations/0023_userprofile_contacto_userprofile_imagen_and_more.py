# Generated by Django 4.2.5 on 2024-01-28 01:41

from django.db import migrations, models
import intranet.validators


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0022_alter_documento_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contacto',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='imagen',
            field=models.ImageField(default='peo', upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='archivo',
            field=models.FileField(upload_to='uploads/% Y/% m/% d/', validators=[intranet.validators.file_size, intranet.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fecha_ingreso',
            field=models.DateField(null=True),
        ),
    ]