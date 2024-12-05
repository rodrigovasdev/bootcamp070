from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login

def registroView(request):
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

# Create your views here.
