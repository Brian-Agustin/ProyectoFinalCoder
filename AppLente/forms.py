from django import forms


class Contactof(forms.Form):
    nombre = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    correo = forms.EmailField()
    mensaje = forms.CharField(max_length=50)

class Turnof(forms.Form):
    nombre = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    correo = forms.EmailField()
    dni = forms.IntegerField()
    fecha = forms.CharField(max_length=50)

class Cotizaf(forms.Form):
    servicio = forms.CharField(max_length=50)
    mensaje = forms.CharField(max_length=50)
