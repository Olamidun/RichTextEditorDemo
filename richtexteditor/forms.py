from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article

        fields = ['title', 'content']