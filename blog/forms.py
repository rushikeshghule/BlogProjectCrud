from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts.

    Includes fields for title and body.
    """
    class Meta:
        model = BlogPost
        fields = ['title', 'body']
