from django.urls import path
from . import views

urlpatterns = [
    path('givebook',views.givebook,name="give"),
    path('returnbook',views.returnbook,name="take"),
    path('clear',views.clear,name="clear"),
    path('book1',views.book1,name="book1"),
    path('book2',views.book2,name="book2"),
    path('book3',views.book3,name="book3"),
]