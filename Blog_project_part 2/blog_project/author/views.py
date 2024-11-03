from django.shortcuts import render,redirect
from .forms import RegisterForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.
def Register(request):
    if request.method == 'POST':
        regiser_from = RegisterForm(request.POST)
        if regiser_from.is_valid():
            messages.success(request, 'User account created successfully.')
            regiser_from.save()
            return redirect('register')
    else:
        regiser_from = RegisterForm()
    
    return render(request, 'register.html', {'form' : regiser_from, 'type' : 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request, 'User account login successfully.')
                login(request, user)
                return redirect('Profile')
            else:
                messages.warning(request, 'User account information incorrect.')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form' : form, 'type' : 'login'})

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_up_from = ChangeUserForm(request.POST, instance = request.user)
        if profile_up_from.is_valid():
            messages.success(request, 'User account update successfully.')
            profile_up_from.save()
            return redirect('Profile')
    else:
        profile_up_from = ChangeUserForm(instance = request.user)
    
    return render(request, 'update_profile.html', {'form' : profile_up_from,})

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            messages.success(request, 'User password update successfully.')
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('Profile')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'pass_change.html', {'form' : form})

def user_logout(request):
    logout(request)
    return redirect('login')