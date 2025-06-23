from django import forms
from .models import Product
class ProductForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, label="Nombre")
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label="Precio")
    description = forms.CharField(widget=forms.Textarea, required=True, label="Descripcion")
    available = forms.BooleanField(initial=True, required=False, label="Disponible")
    image = forms.ImageField(required=False, label="Imagen")
    def __str__(self):
        return self.name
    def save(self): 
        Product.objects.create(
            name=self.cleaned_data['name'],
            price=self.cleaned_data['price'],
            description=self.cleaned_data['description'],
            available=self.cleaned_data['available'],
            image=self.cleaned_data['image'],
        )
        