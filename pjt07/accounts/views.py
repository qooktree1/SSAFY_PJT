from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:  # 로그인 시
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user.is_authenticated:  # 로그인 시
        if request.method == 'POST':
            auth_logout(request)
    return redirect('movies:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')


    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
        
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def update(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)  # 왜 instance = request.user를 넣을까요??
            if form.is_valid():
                form.save()
            return redirect('movies:index')

        else:
            form = CustomUserChangeForm(instance=request.user)
        context ={
            'form': form
        }
        return render(request, 'accounts/update.html', context)


def delete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.user.delete()
            auth_logout(request)
    return redirect('movies:index')


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('movies:index')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/change_password.html', context)