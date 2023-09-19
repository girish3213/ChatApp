from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . models import Profile  
from django.contrib.auth.models import User
from  . forms import RegisterForm, LoginForm
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponse('User authenticated successfully')
            else:
                return HttpResponse('User not authenticated')
    
    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = forms.RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def about_view(request):
    return render(request, 'users/about.html')