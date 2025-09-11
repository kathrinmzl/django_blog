from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) # published
    # queryset = Post.objects.all().order_by("created_on")
    #template_name = "post_list.html" -> replaces by the next html file
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    # get one post returned with that unique slug or an error message if slug doesnt exist
    post = get_object_or_404(queryset, slug=slug)

    return render( # returns an HttpResponse
        request,
        "blog/post_detail.html",
        {"post": post}, # dict with the data -> available for use in the 
        # template as the DTL variable {{ post }}
    )