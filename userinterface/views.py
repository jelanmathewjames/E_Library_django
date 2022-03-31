from django.shortcuts import render, redirect
from Login.models import User

# Create your views here.
def userhome(request):
    id = request.session.get('user_session')
    
    return render(request,'userhome.html')