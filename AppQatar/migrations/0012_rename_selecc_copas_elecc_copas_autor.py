# Generated by Django 4.1 on 2022-10-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppQatar', '0011_remove_seleccion_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copas',
            old_name='selecc',
            new_name='elecc',
        ),
        migrations.AddField(
            model_name='copas',
            name='autor',
            field=models.CharField(default='', max_length=40),
        ),
    ]