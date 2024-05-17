from django.urls import path

from store.views import home_page, sergey, petr, categories

urlpatterns = [
    path("", home_page, ),
    path('sergey/', sergey),
    path('petr/', petr),
    path('categories/', categories),

    # TODO: Создать отдельную вью функцию для каждого маршрута
    path('products/', home_page)
]
