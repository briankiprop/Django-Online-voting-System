from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from forms import RegisterForm, UserTestForm
from django.contrib.auth.decorators import login_required
from .models import Candidate, Vote
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect


# Create your views here.
def HomeView(request):
    chair = Candidate.objects.filter(Category='chairman')
    sec = Candidate.objects.filter(Category='secretary')
    ent = Candidate.objects.filter(Category='Entertainment')
    tre = Candidate.objects.filter(Category='Treasurer')
    aca = Candidate.objects.filter(Category='Academic')
    context = {
        'chair': chair,
        'sec': sec,
        'ent': ent,
        'tre': tre,
        'aca': aca
    }
    return render(request, 'home.html', context)


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


class LoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('home')


class LogoutView(LogoutView):
    template_name = 'logout.html'

    def get_success_url(self):
        return reverse('logout')


@login_required()
def VoteView(request):
    chair = Candidate.objects.filter(Category='chairman')
    sec = Candidate.objects.filter(Category='secretary')
    ent = Candidate.objects.filter(Category='Entertainment')
    tre = Candidate.objects.filter(Category='Treasurer')
    aca = Candidate.objects.filter(Category='Academic')

    context = {
        'chair': chair,
        'sec': sec,
        'ent': ent,
        'tre': tre,
        'aca': aca
    }
    return render(request, 'vote.html', context)


@login_required()
def Votepoll(request):
    try:
        username = request.user.id
        user = User.objects.get(id=username)
        chair = request.POST.get('chairman')
        sec = request.POST.get('secretary')
        ent = request.POST.get('entertainment')
        tre = request.POST.get('treasurer')
        aca = request.POST.get('academics')
        Vote.objects.create(User=user, chairman=chair, secretary=sec, Entertainment=ent, Treasurer=tre, Academic=aca)
    except:
        return HttpResponseRedirect('vote')
    return HttpResponseRedirect('/')

@login_required()
def VotesView(request):
    vote = Vote.objects.all()
    context = {
        'vote': vote
    }
    return render(request, 'votes.html', context)



@login_required()
def InstructionsView(request):
    return render(request, 'instructions.html', {})



def AboutView(request):
    return render(request, 'about.html', {})