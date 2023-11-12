from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render

from main_app.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def post(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'post.html', {'posts': posts})


def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'details.html', {'post': post})
