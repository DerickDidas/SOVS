from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from pollapp.models import Candidate
# Create your views here.
def login(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        NIDA_NUMBER = request.POST['username']

        user = auth.authenticate(password=full_name,username=NIDA_NUMBER)

        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        NIDA_NUMBER = request.POST['NIDA_NUMBER']
        img = request.POST['image']
        user = User.objects.create_user(password=full_name,username=NIDA_NUMBER)
        user.save()
        messages.info(request, 'User Created')
        return redirect('login')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def voted(request):
    vot = User.objects.all()

    if request.method == 'POST':
        request.POST['choice']
        selected_option = vot.get(voted=inputvalue)
        selected_option.voted += 1
        selected_option.save()
        print('user has voted')

    else:
        print('user has already voted')
