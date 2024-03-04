from APP.admins.views.producto.views import ProductListView, FormProduct
from django.urls import path

urlpatterns = [
    path('lst01_inventario/', ProductListView.as_view(), name="lst01_inventario"),    
    path('frm01_inventario/', FormProduct.as_view(), name="form01_inventarios"),    
]
