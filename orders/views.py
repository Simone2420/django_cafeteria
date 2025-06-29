from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from .forms import CreateOrderForm
from django.urls import reverse_lazy

# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"
    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True).first()
        
class CreateOrderView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = CreateOrderForm
    success_url = reverse_lazy("my_order")
    def form_valid(self, form):
        order, created = Order.objects.get_or_create(is_active=True, user=self.request.user)
        form.instance.order = order
        form.instance.quantity = 1
        order.save()
        return super().form_valid(form)
        
