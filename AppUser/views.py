from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            data = form.cleaned_data #diccionario (username: 'asd', password: 'asd')

            #esto si ese dato no viene, solo retorna none, y no se va reventar como en el caso que pongamos data['username']
            usuario = data.get('username')
            contra = data.get('password')

            user = authenticate(username=usuario, password=contra) #devuelve none o user

            if user:        #si existe el usuario
                login(request, user)   #carga mi usuario como variable global

                messages.info(request, 'Inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'Inicio de sesion fallido!') # si ese usuario no existe.. nuser o password estan mal

        else:
            messages.info(request, 'Inicio de sesion fallido!')

        return redirect('inicio')


    contexto = {
        'form': AuthenticationForm(),
        'name_submit': 'login'
    }

    return render(request, "AppUser/login.html", contexto)