"""E_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('Login.urls')),
    path('admin/',include('admin_login.urls')),
    path('usercrud/',include('admin_usercrud.urls')),
    path('bookcrud/',include('admin_bookcrud.urls')),
    path('user/',include('userinterface.urls')),
    path('explore/',include('explore.urls')),
    path('book/',include('book.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
