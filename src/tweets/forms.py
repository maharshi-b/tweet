from django import forms
from .models import Tweet


class TweetModelForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': "What's Happening?",
        })
    )

    class Meta:
        model = Tweet
        fields = [
            'content',
        ]
