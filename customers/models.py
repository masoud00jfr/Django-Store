from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Customer(User):
    date_of_birth = models.DateField(verbose_name='تاریخ تولد', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='address')
    city = models.CharField(max_length=20, verbose_name='شهر')
    street = models.CharField(max_length=20, verbose_name='خیابان')
    post_code = models.CharField(max_length=10, verbose_name='کد پستی')
    default = models.BooleanField(verbose_name='پیش فرض', default=False)

    def __str__(self):
        return f'{self.customer.last_name} - {self.city} - {self.post_code}'

