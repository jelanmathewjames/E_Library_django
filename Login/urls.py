from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('login/<email_token>',views.login,name="login")
]