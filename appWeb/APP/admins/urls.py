from APP.admins.views.producto.views import ProductListView, FormProduct
from APP.admins.views.clientes.views import DeleteClienteView, ClientListView, ClientListPersonalView, CreateClientView
from django.urls import path



urlpatterns = [
    path('lst01_inventario/', ProductListView.as_view(), name="lst01_inventario"),    
    path('frm01_inventario/', FormProduct.as_view(), name="form01_inventarios"),
    path('lst02_clientes_adminuser/', ClientListView.as_view(), name = "lst02_cliente"),    
    path('lst03_clientes_personal/', ClientListPersonalView.as_view(), name = "lst03_personal_cliente"),
    path('frm02__clientes_personal/', CreateClientView.as_view(), name = "form02_clientes"),
    path('dlte01__clientes_personal/<int:pk>/', DeleteClienteView.as_view(), name = "delete01_cliente"),
]
