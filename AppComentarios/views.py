from .forms import FormComentarios
from .models import Comentarios
from django.shortcuts import render, get_objects_or_404
from AppComentarios.models import Post
from django.contrib.contenttypes.models import ContentType

def Post_idd(request, pk):
    instance = get_objects_or_404(Post, pk=pk)
    inicializar_datos = {
        'content_type': instance.get_content_type,
        'object_id': instance.id
    }

    form = FormComentarios(request.POST or None, initial=inicializar_datos)

    if form.is_valid():
        models = form.cleanned_data.get("content_type")
        content_type = ContentType.objects.get(model=models)
        obj_id = form.cleaned_data.get("object_id")
        texto_data = form.cleaned_data.get('texto')

        comentarios, created = Comentarios.objects.get_or_create(
            usuario = request.user,
            content_type = content_type,
            object_id = obj_id,
            texto = texto_data,
        )

        if created:
            print("fue creado con exito")

    context = {
        'form': form,
        'instance': instance
    }

    return render(request, 'comentarios/comentar.html', context)