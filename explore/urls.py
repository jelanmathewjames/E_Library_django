from django.urls import path
from . import views

urlpatterns = [
    path('library',views.library,name="library")
]