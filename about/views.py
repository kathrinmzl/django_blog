from django.shortcuts import render
from .models import About


def about_info(request):
    """
    Display the latest :model:`about.About`.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about_info.html`
    """

    about = About.objects.order_by('-updated_on').first()  # latest first

    return render( # returns an HttpResponse
        request,
        "about/about_info.html",
        {"about": about}, 
    )