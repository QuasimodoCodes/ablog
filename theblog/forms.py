from django import forms    
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'snippet', 'header_image', 'header_video')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Do some BLOGGING!'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Snippet'}), 
        }