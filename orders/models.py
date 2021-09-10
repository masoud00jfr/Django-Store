from django.db import models
from products.models import Product
from customers.models import Customer
# Create your models here.


class Shopping(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.RESTRICT, null=True, blank=True, verbose_name='مشتری')
    date = models.DateTimeField(auto_now_add=True, verbose_name='زمان سفارش')
    total_price = models.DecimalField(verbose_name='مبلغ کل', null=True, blank=True)

    def __str__(self):
        return f'{self.customer.last_name} - {self.date}'


class Order(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE, verbose_name='سفارش مربوطه')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, verbose_name='محصول')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد محصول')

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
