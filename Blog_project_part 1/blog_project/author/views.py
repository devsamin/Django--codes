from django.shortcuts import render,redirect
from .forms import AuthorForm
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        author_from = AuthorForm(request.POST)
        if author_from.is_valid():
            author_from.save()
            return redirect('add_author')
    else:
        author_from = AuthorForm()
    
    return render(request, 'add_author.html', {'form' : author_from})