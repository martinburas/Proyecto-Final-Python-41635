# Generated by Django 4.1 on 2022-10-08 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppQatar', '0013_rename_elecc_copas_selecc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copas',
            name='autor',
        ),
    ]
