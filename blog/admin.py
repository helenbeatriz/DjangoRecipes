from django.contrib import admin
from .models import Post, Comment, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register the Post model with the admin site
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Define the fields to display on the change list page
    list_display = ('title', 'slug', 'status', 'created_on')
    # Define the fields to use for searching
    search_fields = ['title', 'content']
    # Define the filters to use in the right sidebar
    list_filter = ('status', 'created_on')
    # Use the title to populate the slug field
    prepopulated_fields = {'slug': ('title',)}
    # Use Summernote widget for content field
    summernote_fields = ('content',)

# Register the Comment model with the admin site
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Define the fields to display on the change list page
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    # Define the filters to use in the right sidebar
    list_filter = ('approved', 'created_on')
    # Define the fields to use for searching
    search_fields = ('name', 'email', 'body')
    # Define the available actions
    actions = ['approve_comments']

    # Define the action function
    def approve_comments(self, request, queryset):
        # Update the selected comments to be approved
        queryset.update(approved=True)

# Register the Contact model with the admin site
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Define the fields to display on the change list page
    list_display = ['name', 'email', 'subject', 'created_on']
    # Define the filters to use in the right sidebar
    list_filter = ['created_on']
    # Define the fields to use for searching
    search_fields = ['name', 'email', 'subject', 'message']
