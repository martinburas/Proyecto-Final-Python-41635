# Generated by Django 4.1 on 2022-10-08 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppQatar', '0012_rename_selecc_copas_elecc_copas_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copas',
            old_name='elecc',
            new_name='selecc',
        ),
    ]
