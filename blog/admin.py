from django.contrib import admin
# "." indicates that we are importing Post from a file named models, 
# which is in the same directory as our admin.py file
from .models import Post, Comment

# Register your models here.
# Show Post model on admin site
admin.site.register(Post)
admin.site.register(Comment)
