from django.shortcuts import render,redirect
from .forms import RegisterForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

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
# class based loginviews
class UserloginViews(LoginView):
    template_name = 'register.html'
    # success_url = 'Profile'
    def get_success_url(self):
        return reverse_lazy('Profile')

    def form_valid(self, form):
        messages.success(self.request, 'User account login successfully.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'User account information incorrect.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context
    

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

# class based logout views
# class UserlogoutViews(LogoutView):
#     def get_success_url(self):
#         return reverse_lazy('login')
    # next_page = reverse_lazy('login')
