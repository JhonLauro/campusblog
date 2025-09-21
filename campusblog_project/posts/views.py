from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/home.html', {'posts': posts})