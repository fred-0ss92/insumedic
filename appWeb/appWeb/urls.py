"""
URL configuration for appWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from APP.HomePage.views import Pagina_Inicio
from .settings import local
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),
    path('', Pagina_Inicio.as_view(), name = "Index"),
    path('login/', include('APP.login.urls')),
    path('', include("APP.dashboard.urls")),
    path('admins/', include('APP.admins.urls')),
]
if local.DEBUG:
    urlpatterns += static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)