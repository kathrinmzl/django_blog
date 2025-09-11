from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin 

# give admin panel greater functionality and clarity
@admin.register(About) # register the Post model
class AboutAdmin(SummernoteModelAdmin):
    # # Post dashboard functionality
    list_display = ('title',)
    # search_fields = ['title', 'content']
    # list_filter = ('status','created_on',)
    # Add Post functionality
    # prepopulated_fields = {'slug': ('title',)} # creates slug using the title input
    summernote_fields = ('content',) # text-editor

