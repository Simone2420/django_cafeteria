from django.contrib import admin

# Register your models here.
from .models import Order, OrderProduct
class OrderProductInLineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductInLineAdmin,
    ]



admin.site.register(Order, OrderAdmin)
