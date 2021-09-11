from django.db import models
from products.models import Product
from customers.models import Customer
# Create your models here.


class Shopping(models.Model):
    STATUS_CHOICES = (
        ('wait', 'در انتظار پرداخت'),
        ('Paid', 'پرداخت شده'),
        ('cancel', 'لغو شده'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name='shopping', null=True, blank=True, verbose_name='مشتری')
    date = models.DateTimeField(auto_now_add=True, verbose_name='زمان سفارش')
    total_price = models.PositiveIntegerField(verbose_name='مبلغ کل', null=True, blank=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='wait')

    def __str__(self):
        return f'{self.customer.last_name} - {self.date} - {self.status}'


class Order(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE, related_name='order', verbose_name='سفارش مربوطه')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='order', verbose_name='محصول')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد محصول')

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'


class OrderHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shopping = models.OneToOneField(Shopping, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.customer.last_name} - {self.shopping.date}'