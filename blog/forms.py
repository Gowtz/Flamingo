from django import forms
from .models import BlogModel

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content','image']