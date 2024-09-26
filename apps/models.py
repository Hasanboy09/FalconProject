from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model
from django.template.defaultfilters import slugify


class User(AbstractUser):
    image = models.ImageField(upload_to='users/', null=True)
    phone_number = models.CharField(max_length=20, null=True)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True  # o`zi table bo1lib yaratilmasligi kerak # noqa

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)


class Category(BaseModel):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'  # ko`plik shakli ko`rsatiladi

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE, related_name='products')
    shipping_price = models.FloatField()
    quantity = models.IntegerField()
    discount = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        return self.price - (self.discount * self.price / 100)

    # related_name -> category da turib productlarni olishni imkonini beradi


class Specification(Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey('apps.Product', on_delete=models.CASCADE, related_name='specifications')

    def __str__(self):
        return self.key


class ProductImage(Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('apps.Product', on_delete=models.CASCADE,
                                related_name='images')  # 1ta product da ko`p rasm
