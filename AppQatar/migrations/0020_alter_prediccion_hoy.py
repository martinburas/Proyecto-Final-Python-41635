# Generated by Django 4.1 on 2022-10-12 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppQatar', '0019_prediccion_hoy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediccion',
            name='hoy',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.date.today),
        ),
    ]
