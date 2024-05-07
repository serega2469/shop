from django.db import models

from store.constants import (
    CATEGORY_NAME_LEN,
    CATEGORY_SLUG_LEN,
)


class Category(models.Model):
    name = models.CharField(
        'Название',
        max_length=CATEGORY_NAME_LEN,
    )
    slug = models.SlugField(
        max_length=CATEGORY_SLUG_LEN,
        verbose_name='SLUG',
        help_text='slug только из английских букв'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    price = models.PositiveIntegerField('Цена')
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    is_available = models.BooleanField('В наличии', default=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
