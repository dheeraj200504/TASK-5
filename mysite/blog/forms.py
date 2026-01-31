from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
        # Optional: Add custom widgets for better styling
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter post title...',
                'maxlength': '200'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Write your blog content here...',
                'rows': 10
            }),
        }
        
        # Optional: Custom labels
        labels = {
            'title': 'Post Title',
            'content': 'Post Content'
        }