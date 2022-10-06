from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings


# Create your models here.
from AppLente.models import Post


class ComentariosManager(models.Manager):
    def filtro_por_instancia(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(ComentariosManager, self).filter(content_type=content_type, object_id=obj_id)

        return qs

class Comentarios(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name="Comentario")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntergerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    tiempo = models.DateTimeField(auto_now_add=True)

    objects = ComentariosManager()

    class Meta:
        ordering = ['-tiempo']

    def __str__(self):
        return self.texto[:15]

    def comentarios(self):
        instance = self
        qs = Comentarios.objects.filtro_por_instancia(instance)
        return qs

    def get_content_type(self):
        content_type = ContentType.objects.get_for_model(Post)
        return content_type