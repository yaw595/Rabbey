from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Leave a comment...', 'style': "border-radius: 5px !important;"}))
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name', 'style': "border-radius: 5px !important;"}))

    class Meta:
        model = Review
        exclude = ['product']
        fields = ['name', 'text']
