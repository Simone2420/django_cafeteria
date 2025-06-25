from django.urls import path
from .views import MyOrderView, CreateOrderView

urlpatterns = [
    path("mi_orden", MyOrderView.as_view(), name="my_order"),
    path("agregar_producto", CreateOrderView.as_view(), name="create_order"),
]
