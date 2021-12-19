from django.shortcuts import render
from django.http import JsonResponse
from Login.models import User 
from django.contrib.auth.models import auth
from datetime import datetime, timezone
# Create your views here.
def adminlogin(request):
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

def logout(request):
    pass