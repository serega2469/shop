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


# TODO: 1. Улучшить модель,
#  2. написать verbose_name, указать максимальную длину
#  3. Написать Meta класс
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    is_available = models.BooleanField('В наличии', default=True)
