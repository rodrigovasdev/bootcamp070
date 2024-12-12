from django.shortcuts import render, redirect
from .forms import BoardsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,Permission
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.contenttypes.models import ContentType
from .forms import RegistroUsuarioForm
from .models import BoardsModel




# Create your views here.
def boardsform_view(request):
    context ={}
    # crear el objeto form
    form = BoardsForm(request.POST or None, request.FILES or None)
    # verificar si el formulario es valido
    if form.is_valid():
        # guardar los datos del formulario al modelo
        form.save()
        return HttpResponseRedirect('/')
    context = {'formulariogato' : form}
    return render(request, "formulario.html", context)


def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(BoardsModel)
            objecto_permiso = Permission.objects.get(codename='development',content_type=content_type) 
            user = form.save()  # Guardar el usuario
            user.user_permissions.add(objecto_permiso)
            login(request, user)  # Autenticar automáticamente al usuario
            messages.success(request, "Registrado satisfactoriamente.")
            return redirect('/')  # Usa nombres de vistas en lugar de rutas absolutas si es posible
        else:
            messages.error(request, "Registro inválido. Algunos datos ingresados no son correctos.")
    else:
        form = RegistroUsuarioForm()
    
    return render(request, "register.html", {"register_form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Invalido username o password.")
        else:
            messages.error(request,"Invalido username o password.")
    form = AuthenticationForm()
    return render(request, "login.html",{"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/') 

