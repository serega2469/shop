from django.urls import path

from store.views import home_page, sergey, petr, categories


# TODO: Добавить новые маршруты здесь
urlpatterns = [
    path("", home_page,),
    path('sergey/', sergey),
    path('petr/', petr),
    path('categories/', categories),
    path('products/', home_page)
    # path("test/", home_page,),
]
