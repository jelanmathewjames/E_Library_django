from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from Login.models import User
from django.http import JsonResponse
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import auth

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
                user = User.objects.create(first_name=firstname,
                                          last_name=lastname,
                                          email=email,
                                          mobile=phonenumber,
                                          password=password,
                                          email_token=email_token
                                          )
                user.save()
                send_mail_after_registration(email,email_token)
                return JsonResponse(
                    {'success':'True'},
                    safe = False
                )
        elif request.method == 'GET':
            return render(request,'createuser.html')
    elif 'admin_session' not in request.session:
        return redirect

def updateuser(request):
    pass


def deleteuser(request):
    pass


def send_mail_after_registration(email , token):
    subject = 'CEA E_Library Your accounts need to be verified'
    message = f'Hi login through this Link to verify your account http://127.0.0.1:8000/login/{token} \n '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    