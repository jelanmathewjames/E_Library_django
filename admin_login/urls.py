from django.urls import path
from . import views

urlpatterns = [
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminlogout',views.logout,name='adminlogout'),
    path('adminhome',views.adminhome,name="home")
]