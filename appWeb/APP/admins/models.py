from django.db import models
from django.forms import model_to_dict
from appWeb.settings.local import STATIC_URL, MEDIA_URL
from django.utils import timezone

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

