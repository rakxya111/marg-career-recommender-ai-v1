from blogapp.models import Post, Tag 
from django import forms
from django_summernote.widgets import SummernoteWidget


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": 'form-control',
                    'placeholder': 'Enter Tags..'
                }
            ),
        }


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude = ("author", "published_at")
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the title of the post"
            }),
            "description": SummernoteWidget(attrs={
                "summernote": {
                    "width": "100%",
                    "height": "200px"
                }
            }),
            "status": forms.Select(attrs={"class": "form-control"}),
            "tag" : forms.SelectMultiple(attrs={"class":"form-control"}),
        }