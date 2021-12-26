from django.shortcuts import render, redirect

# Create your views here.
def user_data(request):
    return render(request,'admin_data.html')