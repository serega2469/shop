from django.db import models
from django.utils import timezone


class Category(models.Model):
    # TODO: Улушить модель
    name = models.CharField(max_length=30, verbose_name='Название')
    slug = models.SlugField()
    created_at = models.DateTimeField(default=timezone.now)


# TODO: Реализовать модель Product
# TODO: Использовать ForeignKey Product и Category
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
