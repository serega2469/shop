from django.shortcuts import render

from store.models import Product


def home_page(request):
    all_products = Product.objects.all()
    data = {
        'products': all_products,
        'text': 'Все товары'
    }

    return render(
        request,
        'index.html',
        context=data
    )

# TODO: Сделать вывод страницы about/
# TODO: Сделать вывод страницы contact/
# TODO: Создать маршрут products/
# TODO: Создать маршрут categories/ -
#  Вывод категорий и вывод товаров в каждой категоории

# MVC
# Model View Controller
