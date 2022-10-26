from django.shortcuts import render,redirect
from pollapp.models import Position
from pollapp.models import Candidate
from django.contrib.auth.models import User, auth
from django.contrib import messages




# Create your views here.
def home(request):

    return render(request, 'home.html', {})


def face(request):

    return render(request, 'face.html', {})


def contacts(request):

    return render(request, 'contacts.html', {})



def index(request):
    posi = Position.objects.all()

    return render(request, 'index.html', {'posi':posi})


def vote(request,pk):
    posi = Position.objects.all()
    post = Position.objects.get(id=pk)
    cands = post.choices.all()

    if request.user.is_authenticated:
        u = User.objects.get(username = request.user.username)
        u.president = 'True'
        try:
            if request.method == 'POST':
                inputvalue = request.POST['choice']
                selected_option = cands.get(id=inputvalue)
                selected_option.vote_count += 1
                selected_option.save()
                return render(request, 'index.html', {'posi': posi})

        except :
            messages.info(request, "You haven't casted any vote!!Click here to vote again")
            return render(request, 'vote.html', {})


    else:
        print('not logged in')


    return render(request, 'vote.html', {'post': post, 'cands': cands})

def result(request):
    cands = Candidate.objects.all()


    return render(request, 'result.html', {'cands': cands})



