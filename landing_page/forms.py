from django import forms

from .models import AddComment, AddNewPost

class CommentForm(forms.ModelForm):
    class Meta:
        model = AddComment
        fields = ('name', 'email', 'text')

class AddPost(forms.ModelForm):
    class Meta:
        model = AddNewPost
        fields = ('title', 'description')
        labels = {'title': 'Название записи', 'description': 'Описание'}
        help_texts = {'title': 'Укажите краткое название'}