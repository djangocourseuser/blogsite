# blogapp/views.py
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blogapp/index.html', {'posts': posts})

@login_required(login_url='/login/')
def post_detail(request, post_id):
    try:
        post = BlogPost.objects.get(pk=post_id)
    except BlogPost.DoesNotExist:
        post = None
    
    return render(request, 'blogapp/post_detail.html', {'post': post})

@login_required(login_url='/login/')
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    posts = BlogPost.objects.all()
    return render(request, 'blogapp/index.html', {'form': form, 'posts': posts})