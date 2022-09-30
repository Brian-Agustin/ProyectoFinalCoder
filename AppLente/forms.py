from django import forms


class Contactof(forms.Form):
    nombre = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    correo = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ex@example.com'}))
    mensaje = forms.CharField(max_length=50)

class Turnof(forms.Form):
    nombre = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    correo = forms.EmailField()
    dni = forms.CharField(max_length=20)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


sk_import =(
    ("ninguno", "Ninguno seleccionado"),
    ("reparacion", "Reparacion / restauracion"),
    ("compras", "Compras"),
    ("envios", "Envios"),
)
class Cotizaf(forms.Form):
    servicio = forms.ChoiceField(choices=sk_import)
    mensaje = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Escriba aqui'}))

class BuscaTurnoPorDNI(forms.Form):
    dni = forms.CharField(max_length=20)