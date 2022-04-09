from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('data',views.bookdata,name="bookdata"),
    path('createbook',views.createbook,name="createbook"),
    path('deletebook/<id>',views.deletebook,name="deletebook")
]