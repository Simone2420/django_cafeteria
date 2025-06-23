from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    description = models.TextField(verbose_name="Descripcion")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
    image = models.ImageField(upload_to='logo', null=True, blank=True, verbose_name="Imagen")

    def __str__(self):
        return self.name
