#urls
from django.urls import path
from .views import Loginformv1, logoutformv2

urlpatterns=[
    path('', Loginformv1.as_view(), name ='login'),
    path('logouts/', logoutformv2.as_view(), name = "log_out"),
]