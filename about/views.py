from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    # form functionality
    if request.method == "POST":
        # print("Received a POST request")
        collab_form = CollaborateForm(data=request.POST)
        if collab_form.is_valid():
            collab_form.save()
           
            # Success message
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collab_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collab_form": collab_form},
    )