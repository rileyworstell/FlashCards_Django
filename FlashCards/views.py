from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import CardForm
from .models import Cards



def signupuser(request):
    if request.method == "GET":
        return render(request, 'signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': "Username exists already"})
            return render(request, 'signupuser.html', {'form': UserCreationForm()})

        else:
            return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': "passwords didn't match"})

def home(request):
    if request.user.is_authenticated:
        cards = Cards.objects.filter(user=request.user)
    else:
        cards = "cards"
    return render(request, 'home.html', {'cards': cards})


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == "GET":
        return render(request, 'loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
           return render(request, 'loginuser.html', {'form': AuthenticationForm(), 'error': "username and password did not match"})
        else:
            login(request, user)
            return redirect('home') 

def createCard(request):
    if request.method == "GET":
        return render(request, 'create.html', {'form': CardForm()})
    else:
        form = CardForm(request.POST)
        newCard = form.save(commit=False)
        newCard.user = request.user
        newCard.save()
        return redirect('home')

