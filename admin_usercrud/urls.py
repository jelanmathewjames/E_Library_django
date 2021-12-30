from django.urls import path
from . import views
urlpatterns = [
    path('userdata',views.user_data,name='userdata'),
    path('createuser',views.createuser,name='createuser'),
    path('deleteuser/<id>',views.deleteuser,name='deleteuser')
 ]