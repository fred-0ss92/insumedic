from django.db import models
from appWeb.settings.local import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    imagen = models.ImageField(upload_to='usuarios_fotos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Verificando si es un nuevo objeto
            self.set_password(self.password)  # Esto asegura que la contraseña se hashee
        super().save(*args, **kwargs)

    def get_image(self):
        if self.imagen:
            return self.imagen.url
        return '{}{}'.format(STATIC_URL, 'user/empty_user.jpg')