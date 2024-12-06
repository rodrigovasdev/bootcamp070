from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

def signUpView(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario
            login(request, user)  # Autenticar automáticamente al usuario
            messages.success(request, "Registrado satisfactoriamente.")
            return redirect('/signup')  # Usa nombres de vistas en lugar de rutas absolutas si es posible
        else:
            messages.error(request, "Registro inválido. Algunos datos ingresados no son correctos.")
    else:
        form = SignupForm()
    
    return render(request, "signup.html", {"form": form})

def loginView(request):
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
    else:
        form = AuthenticationForm()
        return render(request, "login.html",{"form":form})

def indexView(request):
    return render(request,'index.html')

def logoutView(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/') 

# Create your views here.
