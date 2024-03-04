from django.urls import path
from .views import PanelPrimarioView

urlpatterns = [
    path('admindash/', PanelPrimarioView.as_view(), name = "dash" ),
]
