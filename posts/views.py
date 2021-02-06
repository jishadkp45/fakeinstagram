from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PostAddForm
from .models import Post
# Create your views here.

@login_required
def home_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts':posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:home')
        else:
            return render(request, 'posts/add_post.html', {'form': form})
    else:
        form = PostAddForm()
        return render(request, 'posts/add_post.html', {'form': form})