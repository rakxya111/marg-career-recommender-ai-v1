from .models import Post, Tag , Contact , Newletter , Comment
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
    tag = forms.CharField(required=False, widget=forms.SelectMultiple(attrs={
        'class': 'form-control tag-select',
        'multiple': 'multiple'
    }))

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
        }

    def clean_tag(self):
        tag_data = self.data.getlist('tag')  # Raw list from POST
        tag_objects = []
        for tag_name in tag_data:
            tag_obj, _ = Tag.objects.get_or_create(name=tag_name.strip())
            tag_objects.append(tag_obj)
        return tag_objects

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewLetterForm(forms.ModelForm):
    class Meta:
        model = Newletter
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'