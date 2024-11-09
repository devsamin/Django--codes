from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_from = PostForm(request.POST)
        if post_from.is_valid():
            post_from.instance.author = request.user
            post_from.save()
            return redirect('Profile')
    else:
        post_from = PostForm()
    
    return render(request, 'add_post.html', {'form' : post_from})

# class based createviews
@method_decorator(login_required, name='dispatch')
class AddPostCreateViews(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('Profile')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Edit Post
@login_required
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    edit_from = PostForm(instance=post)
    # print(post.title)
    if request.method == 'POST':
        edit_from = PostForm(request.POST, instance=post)
        if edit_from.is_valid():
            edit_from.instance.author = request.user
            edit_from.save()
            return redirect('homepage')
    return render(request, 'add_post.html', {'form' : edit_from})
# class based updateviews
@method_decorator(login_required, name='dispatch')
class UpdatepostViews(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

# class based deleteviews
@method_decorator(login_required, name='dispatch')
class DeletePostviews(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'

class DetialsPostview(DetailView):
    model = Post
    template_name = 'post_details.html'
    pk_url_kwarg = 'id'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekane stor hobe
        comments = post.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context