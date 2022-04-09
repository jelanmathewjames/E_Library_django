from django.shortcuts import render, redirect
from Login.models import User
from admin_bookcrud.models import Book

# Create your views here.
def userhome(request):
    if 'user_session' in request.session:
        #id = request.session.get('user_session')
        user_details = User.objects.get(pk=request.session.get('user_session'))
        no_of_books = Book.objects.all().count()
        book1 = None
        book2 = None
        book3 = None

        if user_details.book1 != None:
            book_id = int(user_details.book1.get('id'))
            date = user_details.book1.get('date')
            book_data = Book.objects.get(pk=book_id)
            book1 = {'bookname':book_data.book_name,'bookauthor':book_data.book_author,'date':date}
        
        if user_details.book2 != None:
            book_id = int(user_details.book2.get('id'))
            date = user_details.book2.get('date')
            book_data = Book.objects.get(pk=book_id)
            book2 = {'bookname':book_data.book_name,'bookauthor':book_data.book_author,'date':date}
        
        if user_details.book3 != None:
            book_id = int(user_details.book3.get('id'))
            date = user_details.book3.get('date')
            book_data = Book.objects.get(pk=book_id)
            book3 = {'bookname':book_data.book_name,'bookauthor':book_data.book_author,'date':date}

        return render(request,'userhome.html',{'book1':book1,'book2':book2,'book3':book3,'no_of_books':no_of_books})
    elif 'user_session' not in request.session:
        return redirect('/')

def userprofile(request):
    if 'user_session' in request.session:
        user_details = User.objects.get(pk=request.session.get('user_session'))
        return render(request,'userprofile.html',{'user_details':user_details})
    elif 'user_session' not in request.session:
        return redirect('/')