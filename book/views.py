from django.http import JsonResponse
from django.shortcuts import redirect, render
from Login.models import User
from admin_bookcrud.models import Book
from datetime import  date
# Create your views here.

def givebook(request):
    if 'admin_session' in request.session:
        if request.method == 'POST':
            userid = request.POST['userid']
            user = User.object.filter(pk=userid).exists()
            if user:
                request.session['userid'] = userid
                return JsonResponse(
                    {'success':'True'},
                    safe = False
                )
            elif not user:
                return JsonResponse(
                    {'success':'False'},
                    safe = False
                )
        elif request.method == 'GET':
            user = None
            book1 = None
            book2 = None
            book3 = None
            if 'userid' in request.session:
                user = User.object.get(pk=request.session['userid'])
                bookid1 = user.book1
            
                if bookid1 != None:
                    book1 = Book.objects.get(pk=int(bookid1.get('id')))

                bookid2 = user.book2

                if bookid2 != None:
                    book2 = Book.objects.get(pk=int(bookid2.get('id')))

                bookid3 = user.book3

                if bookid3 != None:
                    book3 = Book.objects.get(pk=int(bookid3.get('id')))

            return render(request,'givebook.html',{'user':user,'book1':book1,'book2':book2,'book3':book3})
    
    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')
    

def clearuser(request):
    if 'admin_session' in request.session:
        if request.method == 'GET':
            try:
                del request.session['userid']
                return JsonResponse(
                    {'success':'True'},
                    safe = False
                )
            except KeyError:
                return redirect('/book/givebook')
    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')

def book1(request):
    if 'admin_session' in request.session:
        if request.method == 'POST':
            book1 = request.POST['book1']
            if Book.objects.filter(pk=book1).exists():
                book = Book.objects.get(pk=book1)
                if book.book_inhand == False:
                    Book.objects.filter(
                        pk=book1).update(book_inhandid=request.session['userid']
                        ,book_inhand=True)
                    User.objects.filter(
                        pk=request.session['userid']).update(book1={
                        'id':book1,'date':str(date.today())})
                    return JsonResponse(
                        {'success':'True'},
                        safe = False
                    )
                else:
                    return JsonResponse(
                        {'success':'Alreadyinhand'},
                        safe = False
                    )
            else:
                return JsonResponse(
                    {'success':'False'},
                    safe = False
                )
    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')

def book2(request):
    if 'admin_session' in request.session:
        if request.method == 'POST':
            book2 = request.POST['book2']
            if Book.objects.filter(pk=book2).exists():
                book = Book.objects.get(pk=book2)
                if book.book_inhand == False:
                    Book.objects.filter(
                        pk=book2).update(book_inhandid=request.session['userid']
                        ,book_inhand=True)
                    User.objects.filter(
                        pk=request.session['userid']).update(book2={
                        'id':book2,'date':str(date.today())})
                    return JsonResponse(
                        {'success':'True'},
                        safe = False
                    )
                else:
                    return JsonResponse(
                        {'success':'Alreadyinhand'},
                        safe = False
                )
            else:
                return JsonResponse(
                    {'success':'False'},
                    safe = False
                )
    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')

def book3(request):
    if 'admin_session' in request.session:
        if request.method == 'POST':
            book3 = request.POST['book3']  
            if Book.objects.filter(pk=book3).exists():
                book = Book.objects.get(pk=book3)
                if book.book_inhand == False:
                    Book.objects.filter(
                        pk=book3).update(book_inhandid=request.session['userid']
                        ,book_inhand=True)
                    User.objects.filter(
                        pk=request.session['userid']).update(book3={
                        'id':book3,'date':str(date.today())})
                    return JsonResponse(
                        {'success':'True'},
                        safe = False
                    )
                else:
                    return JsonResponse(
                        {'success':'Alreadyinhand'},
                        safe = False
                    )
            else:
                return JsonResponse(
                    {'success':'False'},
                    safe = False
                )
    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')

def returnbook(request):
    if 'admin_session' in request.session:
        if request.method == 'POST':
            bookid = request.POST['bookid']
            book = Book.objects.filter(pk=bookid).exists()
            if book:
                request.session['bookid'] = bookid
                return JsonResponse(
                    {'success':'True'},
                    safe = False
                )
            elif not book:
                return JsonResponse(
                    {'success':'False'},
                    safe = False
                )
        elif request.method == 'GET':
            user = None
            book = None
            book_slot = None
            book_givendate = None

            if 'bookid' in request.session:
                book = Book.objects.get(pk=request.session['bookid'])

                if book.book_inhand:
                    userid = book.book_inhandid
                    user = User.objects.get(pk=userid)

                    book1 = user.book1
                    book2 = user.book2
                    book3 = user.book3

                    if book1 != None:
                        if int(book1.get('id')) == book.id:
                            book_slot = '1 st SLOT'
                            book_givendate = user.book1.get('date')
                        
                    if book2 != None:
                        if int(book2.get('id')) == book.id:
                            book_slot = '2 st SLOT'
                            book_givendate = user.book2.get('date')
                    if book3 != None:
                        if int(book3.get('id')) == book.id:
                            book_slot = '3 st SLOT'
                            book_givendate = user.book3.get('date')
                        
                elif not book.book_inhand:
                    user = False
            return render(request,'returnbook.html',{'user':user,'book':book,'book_slot':book_slot,'book_givendate':book_givendate})

    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')

def confirmreturn(request):
    if 'admin_session' in request.session:
        if request.method == 'POST':
            book = Book.objects.get(pk=request.session['bookid'])
            userid = book.book_inhandid
            user = User.objects.get(pk=userid)

            book1 = user.book1
            book2 = user.book2
            book3 = user.book3

            if book1 != None:
                if int(book1.get('id')) == book.id:
                    User.objects.filter(pk=userid).update(book1=None)
            if book2 != None:
                if int(book2.get('id')) == book.id:
                    User.objects.filter(pk=userid).update(book2=None)
            if book3 != None:
                if int(book3.get('id')) == book.id:
                    User.objects.filter(pk=userid).update(book3=None)

            Book.objects.filter(pk=request.session['bookid']).update(book_inhandid=None,book_inhand=False)
            return JsonResponse(
                {'success':'True'},
                safe = False
            )
    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')


def clearbook(request):
    if 'admin_session' in request.session:
        if request.method == 'GET':
            try:
                del request.session['bookid']
                return JsonResponse(
                    {'success':'True'},
                    safe = False
                )
            except KeyError:
                return redirect('/book/givebook')
    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')

