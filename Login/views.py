from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.models import auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            
            if user.is_verified:
                request.session['user_session'] = email
    elif request.method == 'GET':
        return render(request,'login.html')

def login(request, email_token):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request,'login.html')