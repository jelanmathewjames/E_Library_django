from django.shortcuts import render, redirect
from admin_bookcrud.models import Book
# Create your views here.

def library(request):
    if 'user_session' in request.session:
        book = Book.objects.all()
        return render(request,'library.html',{'bookdata':book})

    elif 'user_session' not in request.session:
        return redirect('/')