from django.shortcuts import render, redirect
from django.http import JsonResponse
from Login.models import User 
from django.contrib.auth.models import auth
from datetime import datetime, timezone


# Create your views here.
def adminlogin(request):
    if 'admin_session' not in request.session:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email,password=password)
            if user is not None:
                if user.is_superuser:
                    current_datetime = datetime.now(timezone.utc)
                    User.objects.filter(id=user.id).update(last_login=current_datetime)
                    request.session['admin_session'] = email
                    return JsonResponse(
                        {'success':'True'},
                        safe = False,
                    )
                else:
                    return JsonResponse(
                        {'success':'False'},
                        safe = False,
                    )
            else:
                return JsonResponse(
                    {'success':'False'},
                    safe = False,
                )
        elif request.method == 'GET':
            return render(request,'admin_login.html')
    elif 'admin_session' in request.session:
        return redirect('/admin/adminhome')


        
def logout(request):
    if 'admin_session' in request.session:
        try:
            request.session.flush()
            return redirect('/admin/adminlogin')
        except KeyError:
            pass
    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')


def adminhome(request):
    if 'admin_session' in request.session:
        return render(request,'admin_home.html')

    elif 'admin_session' not in request.session:
        return redirect('admin/adminlogin')