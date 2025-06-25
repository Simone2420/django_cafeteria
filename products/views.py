from django.shortcuts import render
from django.views.generic import FormView, ListView
from .forms import ProductForm
from django.urls import reverse_lazy
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.
class ProductFormView(FormView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy("product_create")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductListApi(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)