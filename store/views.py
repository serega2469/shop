from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product, Category


def home_page(request) -> HttpResponse:
    data = {
        'products': Product.objects.all(),
        'text': 'Все товары'
    }
    return render(
        request,
        'index.html',
        context=data
    )


def sergey(request) -> HttpResponse:
    return render(request, 'about_us/about.html')


def petr(request):
    return render(request, 'contact/info.html')


def categories(request):
    data = {
        'categories': Category.objects.all(),
        'text': 'Все категории'
    }
    return render(
        request,
        'categories/categories.html',
        context=data
    )
