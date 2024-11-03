from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(request, category_slug = None):
    data = Post.objects.all()
    
    if category_slug is not None:
        categoris = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = categoris)
    categoris = Category.objects.all()

    # print(data)
    # for post in data:
    #     print(post.title)
    #     for cat in post.category.all():
    #         print(cat.name)
    #     print()
    return render(request, 'home.html', {'data' : data, 'category' : categoris})