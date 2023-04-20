from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib import admin

# status choices for Post model
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # post title
    slug = models.SlugField(max_length=200, unique=True)  # URL slug for post
    author = models.ForeignKey(  # author of post
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')  # featured image for post
    excerpt = models.TextField(blank=True)  # post excerpt
    updated_on = models.DateTimeField(auto_now=True)  # timestamp for when post was last updated
    content = models.TextField()  # post content
    created_on = models.DateTimeField(auto_now_add=True)  # timestamp for when post was created
    status = models.IntegerField(choices=STATUS, default=0)  # post status
    likes = models.ManyToManyField(  # users who have liked this post
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]  # order posts by creation time (most recent first)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()  # return number of likes for this post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")  # post that this comment belongs to
    name = models.CharField(max_length=80)  # commenter's name
    email = models.EmailField()  # commenter's email
    body = models.TextField()  # comment body
    created_on = models.DateTimeField(auto_now_add=True)  # timestamp for when comment was created
    approved = models.BooleanField(default=False)  # whether this comment has been approved

    class Meta:
        ordering = ["created_on"]  # order comments by creation time (most recent first)

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on')  # fields to display in the admin list view
    list_filter = ('created_on',)  # fields to filter by in the admin list view
    search_fields = ('name', 'email', 'subject', 'message')  # fields to search by in the admin list view

class Contact(models.Model):
    name = models.CharField(max_length=255)  # sender's name
    email = models.EmailField(max_length=255)  # sender's email
    subject = models.CharField(max_length=255)  # email subject
    message = models.TextField()  # email body
    created_on = models.DateTimeField(auto_now_add=True)  # timestamp for when email was sent

    def __str__(self):
        return self.name
