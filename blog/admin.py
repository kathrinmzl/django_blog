from django.contrib import admin
# "." indicates that we are importing Post from a file named models, 
# which is in the same directory as our admin.py file
from .models import Post, Comment
# define the summernote text editor, enabling you to access its functionality 
# in the admin panel for your posts
from django_summernote.admin import SummernoteModelAdmin 

# give admin panel greater functionality and clarity
@admin.register(Post) # register the Post model
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    # Post dashboard functionality
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status','created_on',)
    # Add Post functionality
    prepopulated_fields = {'slug': ('title',)} # creates slug using the title input
    summernote_fields = ('content',) # text-editor

# Register your models here.
# Show Post model on admin site
# admin.site.register(Post) -> not neccessary anymore because of decorator
admin.site.register(Comment)

