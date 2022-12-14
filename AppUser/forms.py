from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    imagen = forms.ImageField()

    class Meta:
        model = User
        fields = ('email', 'username', 'imagen')

        help_texts = {k: "" for k in fields}
