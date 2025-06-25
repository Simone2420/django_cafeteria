from django.urls import path
from .views import MyOrderView

urlpatterns = [
    path("mi_orden", MyOrderView.as_view(), name="my_order"),
]
