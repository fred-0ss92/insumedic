from django.db import models
from django.forms import model_to_dict
from appWeb.settings.local import STATIC_URL, MEDIA_URL
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from APP.user.models import User

ESTADO_DEUDA_CHOICES = [
        ('DEUDA', 'Deuda'),
        ('SIN DEUDA', 'Sin Deuda'),
    ]

class Marca(models.Model):
    marca = models.CharField(max_length = 45, verbose_name = "Marca", null = True)

    def __str__(self):
        return self.marca
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']

class Provedor(models.Model):
    prov = models.CharField(max_length = 45, verbose_name = "Proovedor", null = True)

    def __str__(self):
        return self.prov
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Proovedor'
        verbose_name_plural = 'Proovedores'
        ordering = ['id']

#cheacar las categorias, el MEDIA URL Y EL STATIC URL
class Productos(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    image = models.ImageField(upload_to=f'product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    desc = models.TextField(verbose_name = "Descripción", null = True, blank = True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    exist = models.IntegerField(default = 0, verbose_name = "Existencias")
    fecha = models.DateTimeField(default=timezone.now, verbose_name = "Fecha de adquisición")
    compra_pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de compra')
    provedor = models.ForeignKey(Provedor, verbose_name= 'Proovedor', on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, verbose_name="Marca", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        item['pvp'] = format(self.pvp, '.2f')
        item['compra_pvp'] = format(self.compra_pvp, '.2f')
        item['provedor'] = str(self.provedor) if self.provedor else None
        item['marca'] = self.marca.toJSON()
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Clientes(models.Model):
    nombre = models.CharField(verbose_name = 'Clientes', max_length=50, blank = False, null = False)
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    cel = models.CharField(verbose_name = "Celular", max_length=50)
    mail = models.EmailField()
    direc = models.CharField(verbose_name = "Dirección", max_length=80, blank=True, null=True)
    tel_empresa = models.CharField(verbose_name = "Telefono empresa", max_length=50)
    nombre_empresa = models.CharField(verbose_name = 'Empresa', max_length=50, null = True, blank = True)
    vendedor = models.ForeignKey(User, verbose_name="Vendedor", on_delete=models.CASCADE)
    estado_deuda = models.CharField(verbose_name = "Estado",max_length=15, choices=ESTADO_DEUDA_CHOICES, default='SIN DEUDA')

    def __str__(self):
        return f'{self.nombre}: \n Celular: {self.cel} \n Estado: {self.estado_deuda}'
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
    
    def toJSON(self):
        items = model_to_dict(self)
        return items
