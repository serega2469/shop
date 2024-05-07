from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')


# TODO: Сделать вывод страницы about/
# TODO: Сделать вывод страницы contact/

# MVC
# Model View Controller
#