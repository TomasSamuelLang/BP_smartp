from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    login = forms.EmailField(label="Type in your email ", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label="Type in your password ", max_length=100)
    passwordVerification = forms.CharField(widget=forms.PasswordInput(), label="Repeat password ", max_length=100)

    class Meta:
        fields = ('login', 'password')
        model = User


class LoginForm(forms.ModelForm):
    login = forms.EmailField(label="Type in your email", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label="Type in password", max_length=100)

    class Meta:
        fields = '__all__'
        model = User

