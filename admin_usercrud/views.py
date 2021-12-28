from django.shortcuts import render, redirect
from Login.models import User

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
            pass
        elif request.method == 'GET':
            return render(request,'createuser.html')
    elif 'admin_session' not in request.session:
        return redirect

def updateuser(request):
    pass


def deleteuser(request):
    pass
