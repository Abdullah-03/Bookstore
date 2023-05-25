from django import forms
from django.http import request

from .models import Book


class ReviewForm(forms.Form):
    review = forms.CharField(widget=forms.Textarea({'rows': 3}))
