from django import forms


class Contactoformulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    correo = forms.EmailField()
    mensaje = forms.CharField(max_length=50)