from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('verify/<email_token>',views.verify,name="verify")
]