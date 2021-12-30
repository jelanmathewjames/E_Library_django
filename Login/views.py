from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.models import auth
from django.http import JsonResponse


# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        check_email = User.objects.filter(email=email).exists()
        check_user = auth.authenticate(email=email,password=password)

        if check_email:
            if check_user is not None:
                if check_user.is_verified:
                    request.session['user_session'] = email
                    return JsonResponse(
                        {'success':'True'},
                        safe = False,
                    )

                else:
                    return JsonResponse(
                        {'success':'Verify'},
                        safe = False,
                    )
            else:          
                return JsonResponse(
                        {'success':'Password'},
                        safe = False,
                    )
        elif check_email == False:
            return JsonResponse(
                        {'success':'Email'},
                        safe = False,
                    )

    elif request.method == 'GET':
        return render(request,'login.html')




def verify(request, email_token):
    token_verification = User.objects.filter(email_token=email_token).first()
    if token_verification:
        if token_verification.is_verified:
            return render(request,'verify.html',{'message':'E-mail Already Verified'})
        else:
            token_verification.is_verified = True
            token_verification.save()
            return render(request,'verify.html',{'message':'Verification Completed'})
    else:
        return redirect('/')


def logout(request):
    pass