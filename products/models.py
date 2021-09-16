from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Category(MPTTModel):
    title = models.CharField(max_length=70, verbose_name='نام دسته', unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=70, verbose_name='نام محصول')
    description = models.TextField(verbose_name='معرفی محصول', null=True, blank=True)
    stock = models.PositiveIntegerField(default=1, verbose_name='موجودی کالا')
    price = models.PositiveIntegerField(verbose_name='قیمت', null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')
    modified_at = models.DateField(auto_now=True, verbose_name='آخرین تغییر')
    is_active = models.BooleanField(default=True, verbose_name='در دسترس')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='product', verbose_name='دسته بندی')

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    name = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    photo = models.ImageField(upload_to='products')
    is_main = models.BooleanField(default=True)

    def __str__(self):
        if self.is_main:
            return f'{self.product.name}-{self.name}-(Main)'
        return f'{self.product.name}-{self.name}'
