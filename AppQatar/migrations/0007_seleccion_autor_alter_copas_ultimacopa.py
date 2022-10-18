# Generated by Django 4.1 on 2022-10-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppQatar', '0006_seleccion_imagen2_alter_estadio_ciudad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seleccion',
            name='autor',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='copas',
            name='ultimaCopa',
            field=models.IntegerField(verbose_name='Última copa conseguida'),
        ),
    ]
