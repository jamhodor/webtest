from django.shortcuts import render
from homepage.models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, 'homepage/home.html', context)

def tinymce(request):
    return render(request, 'homepage/tinymce.html')
