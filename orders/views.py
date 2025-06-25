from django.shortcuts import render
from django.views.generic import DetailView
from .models import Order
# Create your views here.
class MyOrderView(DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"
    def get_object(self, queryset=None):
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user, is_active=True).first()
        else:
            return None
