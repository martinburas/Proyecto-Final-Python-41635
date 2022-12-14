# Generated by Django 4.1 on 2022-10-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppQatar', '0004_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadio',
            name='imagen',
            field=models.ImageField(null=True, upload_to='estadios'),
        ),
        migrations.AlterField(
            model_name='copas',
            name='cantCopas',
            field=models.IntegerField(verbose_name='Cantidad de copas'),
        ),
        migrations.AlterField(
            model_name='copas',
            name='selecc',
            field=models.CharField(max_length=60, verbose_name='Selección'),
        ),
        migrations.AlterField(
            model_name='copas',
            name='ultimaCopa',
            field=models.IntegerField(verbose_name='Última copa'),
        ),
    ]
