from django.shortcuts import render, redirect
from first_app.forms import ResgisterForm, Userchangdata
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def home(request):
    return render(request, 'first_app/home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = ResgisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account create successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = ResgisterForm()
        return render(request, 'first_app/singup.html', {'form' : form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = name, password = user_pass) # check korteci user database e ache ki na


                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'first_app/login.html', {'form' : form})
    else:
        return redirect('profile')
    
    

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Userchangdata(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account update successfully')
                form.save()
        else:
            form = Userchangdata(instance=request.user)
        return render(request, 'first_app/profile.html', {'form' : form})
    else:
        return redirect('signup')

def user_logout(request):
    logout(request)
    return redirect('login')


def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user= request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'first_app/changepass.html', {'form' : form})
    else:
        return redirect('login')
    
def change_pass2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user= request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request, 'first_app/changepass.html', {'form' : form})
    else:
        return redirect('login')

# def user_change_data(request):
    