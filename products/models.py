from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=70, verbose_name='نام محصول')
    description = models.TextField(verbose_name='معرفی محصول', null=True, blank=True)
    stock = models.PositiveIntegerField(default=1, verbose_name='موجودی کالا')
    price = models.PositiveIntegerField(verbose_name='قیمت', null=True, blank=True)
    pub_date = models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')
    is_active = models.BooleanField(default=True, verbose_name='در دسترس')

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    name = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='products')
    is_main = models.BooleanField(default=True)

    def __str__(self):
        if self.is_main:
            return f'{self.product.name}-{self.name}-(Main)'
        return f'{self.product.name}-{self.name}'
