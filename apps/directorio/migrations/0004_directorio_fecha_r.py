# Generated by Django 2.2.4 on 2020-04-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0003_auto_20200401_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorio',
            name='fecha_r',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]