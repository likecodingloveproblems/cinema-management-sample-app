from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "autofocus": True}))
    email = forms.EmailField(label='email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='Confirm', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__exact=email).exists():
            raise forms.ValidationError('Email already exists.')
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return confirm_password
