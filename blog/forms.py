from .models import Comment, Contact
from django import forms

# CommentForm for creating new comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)  # specifying the fields to be included in the form

# ContactForm for sending messages through the contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]  # specifying the fields to be included in the form
