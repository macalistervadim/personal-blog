from django import forms

from .models import AddComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = AddComment
        fields = ('name', 'email', 'text')