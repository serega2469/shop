from django.urls import path

from store.views import home_page


urlpatterns = [
    path("", home_page,),
    # path("test/", home_page,),
]
