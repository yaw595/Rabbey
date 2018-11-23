from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home Address'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', ' placeholder': 'city'}))
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Special Message (Souvenir Order only)'}),
        required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn btn-primary', 'style': 'width: 250px;'}),
                             required=False)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'postal_code', 'city', 'message', 'image']
