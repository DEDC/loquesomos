# Generated by Django 2.2.4 on 2020-04-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0007_auto_20200402_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directorio',
            name='repartidores',
            field=models.ManyToManyField(blank=True, to='directorio.Repartidores', verbose_name='Repartidores'),
        ),
    ]