# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'location']
    
    # Do not define the widget here, handle multiple files directly in the template and view
    images = forms.FileField(required=False)
