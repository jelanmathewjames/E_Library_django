from django.shortcuts import render, redirect
from admin_bookcrud.models import Book
# Create your views here.

def library(request):
    book = Book.objects.all()
    return render(request,'library.html',{'bookdata':book})