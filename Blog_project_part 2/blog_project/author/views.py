from django.shortcuts import render,redirect
from .forms import RegisterForm
# Create your views here.
def Register(request):
    if request.method == 'POST':
        regiser_from = RegisterForm(request.POST)
        if regiser_from.is_valid():
            regiser_from.save()
            return redirect('register')
    else:
        regiser_from = RegisterForm()
    
    return render(request, 'register.html', {'form' : regiser_from})