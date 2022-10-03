from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    correo = models.EmailField()
    mensaje = models.CharField(max_length=50)
    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}, Correo: {self.correo}, mensaje: {self.mensaje}"
class Turno(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    correo = models.EmailField()
    dni = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}, Correo: {self.correo}, dni: {self.dni}, fecha: {self.fecha}"
class Cotiza(models.Model):
    servicio = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=50)
    def __str__(self):
        return f"Servicio: {self.servicio}, mensaje: {self.mensaje}"