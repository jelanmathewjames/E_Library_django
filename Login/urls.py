from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('verify/<email_token>',views.verify,name="verify"),
    path('',views.home,name="home")
]