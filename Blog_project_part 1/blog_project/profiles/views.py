from django.shortcuts import render,redirect
from .forms import ProfileFrom
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profile_form = ProfileFrom(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile')
    else:
        profile_form = ProfileFrom()
    
    return render(request, 'add_profile.html', {'form' : profile_form})