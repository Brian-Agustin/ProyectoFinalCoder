from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email', 'username')

        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField(max_length=30,label="username")
    email = forms.EmailField(label="email")
    password1 = forms.CharField(label ="contraseña",widget=forms.PasswordInput)
    password1 = forms.CharField(label ="contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
        help_texts = {k: "" for k in fields}