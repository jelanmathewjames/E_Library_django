from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from Login.models import User
from django.http import JsonResponse
import uuid
from django.contrib.auth.models import auth
from datetime import datetime, timezone

# Create your views here.
def user_data(request):

    if 'admin_session' in request.session:
        user = User.objects.all()
        return render(request,'admin_userdata.html',{'user':user})

    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')


def createuser(request):

    if 'admin_session' in request.session:
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            password = request.POST['password']

            if User.objects.filter(email=email).exists():
                return JsonResponse(
                    {'success':'email'},
                    safe = False,
                )

            elif User.objects.filter(mobile=phonenumber).exists():
                return JsonResponse(
                    {'success':'phone'},
                    safe = False
                )

            else:
                email_token = str(uuid.uuid4())
                current_time = datetime.now(timezone.utc)
                user = User.objects.create(first_name=firstname,
                                          last_name=lastname,
                                          email=email,
                                          mobile=phonenumber,
                                          password=password,
                                          email_token=email_token,
                                          date_joined=current_time,
                                          )
                user.set_password(password)
                user.save()


                return JsonResponse(
                    {'success':'True'},
                    safe = False
                )

        elif request.method == 'GET':
            return render(request,'createuser.html')

    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')

def updateuser(request):
    
    pass


def deleteuser(request, id):
    if 'admin_session' in request.session:
        User.objects.get(pk=id).delete()
        return redirect('userdata')
        
    elif 'admin_session' not in request.session:
        return redirect('/admin/adminlogin')


#function for sending data
'''def send_mail_after_registration(email , token):

    subject = 'CEA E_Library Your accounts need to be verified'
    message = f'Hi login through this Link to verify your account http://127.0.0.1:8000/verify/{token} \n '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )'''
    