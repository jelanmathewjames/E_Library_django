from django.shortcuts import render, redirect
from Login.models import User

# Create your views here.
def userhome(request):
    if 'user_session' in request.session:
        #id = request.session.get('user_session')
        return render(request,'userhome.html')
    elif 'user_session' not in request.session:
        return redirect('/')

def userprofile(request):
    if 'user_session' in request.session:
        id = request.session.get('user_session')
        user_details = User.objects.get(pk=id)
        return render(request,'userprofile.html',{'user_details':user_details})
    elif 'user_session' not in request.session:
        return redirect('/')