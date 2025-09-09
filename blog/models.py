from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# class named Post inheriting from the Model class
class Post(models.Model):
    # Attributes: 
    # title
    title = models.CharField(max_length=200, unique=True)
    # article still in production
    slug = models.SlugField(max_length=200, unique=True)
    # author defined as a Foreign Key to the User model
    # One user can write many posts, so this is a one-to-many or Foreign Key. 
    # The cascade on delete means that on the deletion of the user entry, all 
    # their posts are also deleted.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # content blog article
    content = models.TextField()
    # create time
    # auto_now_add=True means the default created time is the time of post entry.
    created_on = models.DateTimeField(auto_now_add=True)
    # status
    # uses a constant STATUS
    status = models.IntegerField(choices=STATUS, default=0)
    # excerpt
    excerpt = models.TextField(blank=True)
    # updated_on
    # auto_now argument for the updated_on field sets the value to the current 
    # date and time whenever the record is saved, not just when it is created.
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )

    body = models.TextField()
    
    approved = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    