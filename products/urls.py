from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path('agregar/', ProductFormView.as_view(), name='product_create'),
]
