from django import forms
from django.conf import settings


class FindSimilarSimpleForm(forms.Form):

    text = forms.CharField(max_length=settings.MAX_TEXT_LENGTH, widget=forms.TextInput(attrs={'class': 'form-control'}))
    texts = forms.CharField(max_length=settings.TEXT_LIST_LENGTH_LENGTH, widget=forms.Textarea(attrs={'class': 'form-control'}))