from django.db import models
from appWeb.settings.local import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    imagen = models.ImageField(upload_to='usuarios_fotos/', null=True, blank=True)

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'user/empty_user.jpg')