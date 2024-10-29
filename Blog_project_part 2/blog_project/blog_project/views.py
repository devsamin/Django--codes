from django.shortcuts import render
from posts.models import Post

def home(request):
    data = Post.objects.all()
    print(data)
    for post in data:
        print(post.title)
        for cat in post.category.all():
            print(cat.name)
        print()
    return render(request, 'home.html', {'data' : data})