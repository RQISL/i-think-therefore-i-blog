from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    pageinate_by = 6
