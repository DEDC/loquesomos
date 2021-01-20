# Generated by Django 2.2.4 on 2020-03-31 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('logo', models.ImageField(null=True, upload_to='directorio/categoria', verbose_name='Imagen')),
                ('codename', models.CharField(max_length=10, verbose_name='Código para control interno')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cate', to='directorio.Categorias', verbose_name='Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Directorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('municipio', models.CharField(choices=[('balancan', 'Balancán'), ('cardenas', 'Cárdenas'), ('centla', 'Centla'), ('centro', 'Centro'), ('comalcalco', 'Comalcalco'), ('cunduacan', 'Cunduacán'), ('emiliano_zapata', 'Emiliano Zapata'), ('huimanguillo', 'Huimanguillo'), ('jalapa', 'Jalapa'), ('jalpa_mendez', 'Jalpa de Méndez'), ('jonuta', 'Jonuta'), ('macuspana', 'Macuspana'), ('nacajuca', 'Nacajuca'), ('paraiso', 'Paraíso'), ('tacotalpa', 'Tacotalpa'), ('teapa', 'Teapa'), ('tenosique', 'Tenosique')], max_length=30, verbose_name='Municipio')),
                ('facebook_url', models.URLField(blank=True, null=True, verbose_name='Link de facebook')),
                ('instagram_url', models.URLField(blank=True, null=True, verbose_name='Link de instagram')),
                ('logo', models.ImageField(null=True, upload_to='directorio/logos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directorio.Categorias', verbose_name='Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Repartidores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('logo', models.ImageField(null=True, upload_to='directorio/repartidores', verbose_name='Logo')),
                ('app_url', models.URLField(blank=True, null=True, verbose_name='Link a la app')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono')),
            ],
        ),
        migrations.CreateModel(
            name='Imagenes_Directorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='directorio/imagenes', verbose_name='Imagen')),
                ('directorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dir_imagenes', to='directorio.Directorio')),
            ],
        ),
        migrations.AddField(
            model_name='directorio',
            name='repartidores',
            field=models.ManyToManyField(to='directorio.Repartidores', verbose_name='Repartidores'),
        ),
    ]
