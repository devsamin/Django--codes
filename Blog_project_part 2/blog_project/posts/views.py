from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_from = PostForm(request.POST)
        if post_from.is_valid():
            post_from.save()
            return redirect('add_post')
    else:
        post_from = PostForm()
    
    return render(request, 'add_post.html', {'form' : post_from})

# Edit Post

def edit_post(request, id):
    post = Post.objects.get(pk=id)
    edit_from = PostForm(instance=post)
    # print(post.title)
    if request.method == 'POST':
        edit_from = PostForm(request.POST, instance=post)
        if edit_from.is_valid():
            edit_from.save()
            return redirect('homepage')

    
    return render(request, 'add_post.html', {'form' : edit_from})

def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')