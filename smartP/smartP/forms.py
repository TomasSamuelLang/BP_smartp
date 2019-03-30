from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # username = forms.CharField(label="Type in your username ", max_length=100)
    email = forms.EmailField(label="Type in your email ", max_length=100)

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = User


class LoginForm(forms.ModelForm):
    username = forms.CharField(label="Type in your username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label="Type in password", max_length=100)

    class Meta:
        fields = '__all__'
        model = User

