from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) # published
    # queryset = Post.objects.all().order_by("created_on")
    #template_name = "post_list.html" -> replaces by the next html file
    template_name = "blog/index.html"
    paginate_by = 6