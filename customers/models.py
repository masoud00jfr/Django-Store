from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Shopping

# Create your models here.

User = get_user_model()


class Customer(User):
    pass


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=20, verbose_name='شهر')
    street = models.CharField(max_length=20, verbose_name='خیابان')
    post_code = models.CharField(max_length=10, verbose_name='کد پستی')

    def __str__(self):
        return f'{self.customer.last_name} - {self.city} - {self.post_code}'


class OrderHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shopping = models.OneToOneField(Shopping, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.customer.last_name} - {self.shopping.date}'
