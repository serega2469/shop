from django.db import models


class Category(models.Model):
    # TODO: Улушить модель
    name = models.CharField(max_length=30, verbose_name='Название')
    slug = models.SlugField()


# TODO: Реализовать модель Product
# TODO: Использовать ForeignKey Product и Category
