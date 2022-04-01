from django.shortcuts import render, redirect
from Login.models import User

# Create your views here.
def userhome(request):
    if 'user_session' in request.session:
        id = request.session.get('user_session')
        return render(request,'userhome.html')
    elif 'user_session' not in request.session:
        return redirect('/')