from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, SignInForm, LibroForm, PrestamoForm, PrestamoUsuarioForm
from .models import Libro, Prestamo
# Create your views here.

def lista_usuario(request):
    if request.user.has_perm('auth.view_user'):
        usuarios = User.objects.all()
    else:
        usuarios = User.objects.filter(id=request.user.id)
    return render(request, 'usuarios_lista.html', {'usuarios': usuarios})

def nuevo_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios_nuevo.html', {'form': form})

def login_usuario(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_usuarios')
            else:
                return render(request, 'usuarios_ingresar.html', {'form': form, 'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'usuarios_ingresar.html', {'form': form})

def logout_view(request):
    logout(request) 
    messages.success(request, "Has cerrado sesión correctamente.") 
    return redirect('login') 

def lista_libros(request):
    libros = Libro.objects.all()
    context = {'libros': libros}
    return render(request, 'libros_lista.html', context)

def nuevo_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = Libro()
            libro.titulo = form.cleaned_data['titulo']
            libro.autor = form.cleaned_data['autor']
            libro.isbn = form.cleaned_data['isbn']
            libro.disponible = form.cleaned_data['disponible']
            libro.save()
            messages.success(request, "Libro creado correctamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros_nuevo.html', {'form': form})

def editar_libro(request,id):
    libro = Libro.objects.get(id=id)
    form = LibroForm(instance=libro)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado correctamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
        return render(request, 'libros_editar.html', {'form': form} )
    
def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    messages.success(request, "Libro eliminado correctamente.")
    return redirect('lista_libros')

def lista_prestamos(request):
    if request.user.has_perm('biblioteca.view_prestamo'):
        prestamos = Prestamo.objects.all()
    else:
        prestamos = Prestamo.objects.filter(usuario=request.user)
    return render(request, 'prestamos_lista.html', {'prestamos': prestamos})

def nuevo_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.usuario = request.user
            prestamo.save()
            messages.success(request, "Préstamo creado correctamente.")
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'prestamos_nuevo.html', {'form': form})

def editar_prestamo(request,id):
    prestamo = Prestamo.objects.get(id=id)
    form = PrestamoForm(instance=prestamo)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, "Préstamo actualizado correctamente.")
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
        return render(request, 'prestamos_editar.html', {'form': form} )
    
def eliminar_prestamo(request,id):
    prestamo = Prestamo.objects.get(id=id)
    prestamo.delete()
    messages.success(request, "Préstamo eliminado correctamente.")
    return redirect('lista_prestamos')

def nuevo_usuario_prestamo(request, id):
    libro = get_object_or_404(Libro, id=id)  # Obtén el libro desde la base de datos
    usuario = request.user  # Obtén el usuario autenticado

    if request.method == 'POST':
        form = PrestamoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')  # Redirige a la lista de préstamos
    else:
        # Pre-rellenar el formulario con el usuario y el libro seleccionados
        form = PrestamoUsuarioForm(initial={'usuario': usuario, 'libro': libro})

    return render(request, 'prestamos_nuevo_usuario.html', {'form': form})

def detalle_libro(request, id):
    libro = Libro.objects.get(id=id)
    return render(request, 'libros_detalle.html', {'libro': libro})