from django.forms import ModelForm
from .models import OrderProduct

class CreateOrderForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ["product"]