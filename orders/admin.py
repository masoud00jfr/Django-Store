from django.contrib import admin
from .models import Order, OrderHistory, Shopping
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Shopping)
class ShoppingAdmin(admin.ModelAdmin):
    pass
