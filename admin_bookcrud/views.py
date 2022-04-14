from django.http import JsonResponse
from django.shortcuts import render , redirect
from . models import Book
from . forms import BookForm
from Login.models import User
# Create your views here.


def bookdata(request):
    if 'admin_session' in request.session:
        bookdata = Book.objects.all()
        return render(request,'admin_bookdata.html',{'bookdata':bookdata})
    elif 'admin_session' not in request.session:
        return redirect('admin/adminlogin')

def createbook(request):
    if 'admin_session' in request.session:
        if request.method == 'POST':
            form = BookForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/bookcrud/data')
        else:
            form = BookForm()
            return render(request,'bookcrud.html',{'form':form})
    elif 'admin_session' not in request.session:
        return redirect('admin/adminlogin')

def deletebook(request,id):
    if 'admin_session' in request.session:
        book = Book.objects.get(pk=id)
        if book.book_inhand:
            pass

        elif not book.book_inhand:    
            book.delete()
        return redirect('bookdata')
    elif 'admin_session' not in request.session:
        return redirect('admin/adminlogin')