from django.urls import path
from . import views
urlpatterns = [
    path('userhome',views.userhome,name="userhome"),
    path('userprofile',views.userprofile,name="userprofile")
]