from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


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

class Image(models.Model):
    imagefile = models.FileField(upload_to='images/', null=True, verbose_name='')

    def __str__(self):
        return str(self.imagefile)


class Post(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    tiempo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug


def nueva_url(instance, url=None):
    slug = slugify(instance.texto)
    if url is not None:
        slug = url

    qs = Post.objects.filter(slug=slug).order_by('-id')
    if qs.exists():
        nueva_url_si = '%s-%s' % (slug, qs.first().id)
        return nueva_url(instance, url=nueva_url_si)
    return slug


def url_creada(sender, instance, *args, **kwargs):
    if not instance.slug:
        print("my nombre es %s y tengo %s" % ('jorge', 20))
        instance.slug = nueva_url(instance)


pre_save.connect(url_creada, sender=Post)
