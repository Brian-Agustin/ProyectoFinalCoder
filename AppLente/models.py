from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    correo = models.EmailField()
    mensaje = models.CharField(max_length=50)
    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}, Correo: {self.correo}, mensaje: {self.mensaje}"

