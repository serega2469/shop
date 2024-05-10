from django.urls import path

from store.views import home_page


# TODO: Добавить новые маршруты здесь
urlpatterns = [
    path("", home_page,),
    # path("test/", home_page,),
]
