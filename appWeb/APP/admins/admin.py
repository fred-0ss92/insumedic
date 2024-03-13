from django.contrib import admin

# Register your models here.
from APP.admins.models import Clientes
from APP.admins.models import Productos

admin.site.register(Productos)

admin.site.register(Clientes)