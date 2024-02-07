from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, FileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'introduction', 'article_copy', 'cover_img', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'formField',
                'placeholder': 'Article name (max. 100 characters)'
            }),
            "introduction": TextInput(attrs={
                'class': 'formField',
                'placeholder': 'Short introduction (max. 300 characters)'
            }),
            "article_copy": Textarea(attrs={
                'class': 'formField',
                'placeholder': 'Full article'
            }),
            "cover_img": FileInput(attrs={
                'class': 'formField formFieldImage',
                'placeholder': 'Add cover image or GIF'
            }),
            "date": DateTimeInput(attrs={
                'class': 'formField',
                'placeholder': 'Publishing time',
                'type': 'date'
            }),
        }