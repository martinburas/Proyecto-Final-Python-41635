# Generated by Django 4.1 on 2022-10-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppQatar', '0005_estadio_imagen_alter_copas_cantcopas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seleccion',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='banderas', verbose_name='Bandera'),
        ),
        migrations.AlterField(
            model_name='estadio',
            name='ciudad',
            field=models.CharField(max_length=60, verbose_name='Ciudad en la que se encuentra el estadio'),
        ),
        migrations.AlterField(
            model_name='estadio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='estadios', verbose_name='Imagen del estadio'),
        ),
        migrations.AlterField(
            model_name='estadio',
            name='nombre',
            field=models.CharField(max_length=60, verbose_name='Nombre del estadio'),
        ),
    ]
