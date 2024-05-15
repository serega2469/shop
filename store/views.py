from django.shortcuts import render

from store.models import Product, Category


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


def sergey(request):
    return render(request, 'about_us/about.html')


def petr(request):
    return render(request, 'contact/info.html')



def categories(request):
    all_categories = Category.objects.all()
    data = {
        'categories': all_categories,
        'text': 'Все категории'
    }
    return render(request, 'categories/categories.html', context=data)

    # MVC
# Model View Controller
