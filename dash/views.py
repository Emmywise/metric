from django.shortcuts import render, redirect
from django.views import View
from dash.forms import adminLoginForm, updateForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
#import logging #to do some dubugging
#logger = logging.getLogger(__name__) #also for debbuging

# Create your views here.

    
def index(request):
    return render(request, 'dash/index.html' )

@login_required
def adminPage(request):
    return render(request, 'dash/adminPage.html',)

def user_login(request):
    form = adminLoginForm(request.POST)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        #logger.error('Email: ')
        #logger.error(email)
        #logger.error('Password: ')
        #logger.error(password)
        #logger.error('Request: ')
        #logger.error(request.POST)

        user= authenticate(email=email, password=password) #fetch emial and password correspond from db
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dash:adminPage'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dash/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('dash:index')

def new_post(request):  
    if request.method == "POST":
        form = updateForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('dash:index')
    else:
        form = updateForm
    return render(request, 'dash/adminPage.html',  {'form': form})