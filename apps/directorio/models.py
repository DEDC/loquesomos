# Django
from django.db import models

class Directorio(models.Model):
    class Meta:
        ordering = ['nombre']
    municipios_choices = [
        ('balancan', 'Balancán'),
        ('cardenas', 'Cárdenas'), 
        ('centla', 'Centla'), 
        ('centro', 'Centro'),
        ('comalcalco', 'Comalcalco'), 
        ('cunduacan', 'Cunduacán'),
        ('emiliano_zapata', 'Emiliano Zapata'),
        ('huimanguillo', 'Huimanguillo'),
        ('jalapa', 'Jalapa'),
        ('jalpa_mendez', 'Jalpa de Méndez'),
        ('jonuta', 'Jonuta'),
        ('macuspana', 'Macuspana'),
        ('nacajuca', 'Nacajuca'),
        ('paraiso', 'Paraíso'),
        ('tacotalpa', 'Tacotalpa'),
        ('teapa', 'Teapa'),
        ('tenosique', 'Tenosique')
    ]
    nombre = models.CharField('Nombre', max_length = 100)
    telefono = models.CharField('Teléfono', max_length = 10)
    municipio = models.CharField('Municipio', max_length = 30, choices = municipios_choices)
    facebook_url = models.URLField('Link de facebook', null = True, blank = True)
    instagram_url = models.URLField('Link de instagram', null = True, blank = True)
    web_page = models.URLField('Link a página web', null = True, blank = True)
    logo = models.ImageField(upload_to = 'directorio/logos', null = True)
    fecha_r = models.DateTimeField(auto_now_add = True, null = True)
    serv_dom = models.BooleanField(default = False)
    categoria = models.ForeignKey('Categorias', verbose_name = 'Categoría', on_delete = models.PROTECT)
    repartidores = models.ManyToManyField('Repartidores', verbose_name = 'Repartidores', blank = True)

    def get_town(self):
        return dict(self.municipios_choices).get(self.municipio, 'No especificado')

class Imagenes_Directorio(models.Model):
    imagen = models.ImageField('Imagen', upload_to = 'directorio/imagenes')
    directorio = models.ForeignKey('Directorio', related_name = 'dir_imagenes', on_delete = models.CASCADE)

class Categorias(models.Model):
    class Meta:
        ordering = ['id']
    nombre = models.CharField('Nombre', max_length = 100, unique = True)
    categoria = models.ForeignKey('self', verbose_name = 'Categoría', related_name = 'cate', null = True, blank = True, on_delete = models.SET_NULL)
    logo = models.ImageField('Imagen', upload_to = 'directorio/categoria', null = True)
    codename = models.CharField('Código para control interno', max_length = 10, unique = True)

    def __str__(self):
        if self.categoria:
            return '{} ({})'.format(self.nombre, str(self.categoria.nombre).lower())
        else:
            return '{}'.format(self.nombre)

class Repartidores(models.Model):
    nombre = models.CharField('Nombre', max_length = 100)
    logo = models.ImageField('Logo', upload_to = 'directorio/repartidores', null = True)
    app_url = models.URLField('Link a la app', null = True, blank = True)
    telefono = models.CharField('Teléfono', max_length = 10, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.nombre)