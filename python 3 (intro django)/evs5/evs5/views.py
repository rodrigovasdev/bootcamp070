from django.shortcuts import render
import datetime
from .forms import InputForm
def navbarView(request):
    return render(request,'navbar.html')

def indexView(request):
    return render(request,'index.html')

class Persona(object):
    def __init__ (self, nombre, apellido, login):
        self.nombre=nombre
        self.apellido=apellido 
        self.login = login

def mostrarView(request):
    persona = Persona("Juan", "Peréz", True)
    items=['autos','cubos'] 
    horActual = datetime.datetime.now()
    context = {'nombre' : persona.nombre, "apellido" : persona.apellido, 'auth': persona.login, 'lista': items, 'fecha': horActual}
    return render(request, "persona.html", context)


class Libro(object):
    def __init__ (self, titulo, autor, valoracion):
        self.titulo=titulo
        self.autor=autor
        self.valoracion = valoracion
    
def librosView (request):
    # Instancias de libros
    libro1 = Libro("Django 3 Web Development Cookbook Fourth Edition", "Aidas Bendoraitis", 3250)
    libro2 = Libro("Two Scoops of Django 3.x", "Daniel Feldroy", 1570)
    libro3 = Libro("El libro de Django", "Adrian Holovaty", 189)
    libro4 = Libro("Python Web Development with Django", "Jeff Forcier", 900)
    libro5 = Libro("Django for Professionals", "William S. Vincent", 2100)
    libro6 = Libro("Django for APIs", "William S. Vincent", 2540)

    # Lista de libros
    listaLibros = [libro1, libro2, libro3, libro4, libro5, libro6]
    context = {'libros' : listaLibros}
    return render (request,'libros.html',context)

def datosform_view(request):
 # la logica de la vista se implementa aqui
    print(request.POST)
    context = {'gatogatito' : InputForm}
    return render(request, "datosForm.html",context)
