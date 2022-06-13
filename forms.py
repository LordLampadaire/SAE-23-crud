from django import forms
from .models import comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = ["username", "email", "body"]