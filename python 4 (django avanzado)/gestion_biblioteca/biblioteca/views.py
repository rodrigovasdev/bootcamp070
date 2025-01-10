from django.shortcuts import render, redirect
from .models import Libro,Autor, Biblioteca
# Create your views here.
def ver_libros(request):
    libros = Libro.objects.all()
    context = {
        'libros': libros
    }
    return render(request, 'ver_libros.html', context)

def agregar_libro(request):
    autores = Autor.objects.all()
    bibliotecas = Biblioteca.objects.all()
    context = {'autores': autores, 'bibliotecas': bibliotecas}
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        objeto_autor = Autor.objects.get(nombre=autor)
        biblioteca = request.POST.get('biblioteca')
        objeto_biblioteca = Biblioteca.objects.get(nombre=biblioteca)
        fecha_publicacion = request.POST.get('fecha_publicacion')
        estado = request.POST.get('estado')
        categoria = request.POST.get('categoria')
        libro = Libro(titulo=titulo, autor=objeto_autor, biblioteca=objeto_biblioteca, fecha_publicacion=fecha_publicacion, estado=estado, categoria=categoria)
        libro.save()
        return redirect('/biblioteca/')
    
    return render(request, 'agregar_libro.html',context)

def editar_libro(request,pk):
    autores = Autor.objects.all()
    bibliotecas = Biblioteca.objects.all()
    libro = Libro.objects.get(id=pk)
    context = {'libro': libro, 'autores': autores, 'bibliotecas': bibliotecas}
    return render(request=request, template_name='editar_libro.html',context=context)

def actualizar_libro(request, id):
    titulo = request.POST.get('titulo')
    autor = request.POST.get('autor')
    objeto_autor = Autor.objects.get(nombre=autor)
    biblioteca = request.POST.get('biblioteca')
    objeto_biblioteca = Biblioteca.objects.get(nombre=biblioteca)
    fecha_publicacion = request.POST.get('fecha_publicacion')
    estado = request.POST.get('estado')
    categoria = request.POST.get('categoria')

    libro = Libro.objects.get(id=id)
    libro.titulo = titulo
    libro.autor = objeto_autor
    libro.biblioteca = objeto_biblioteca
    libro.fecha_publicacion = fecha_publicacion
    libro.estado = estado
    libro.categoria = categoria
    libro.save()
    return redirect('/biblioteca/')

def eliminar_libro(request,pk):
    libro = Libro.objects.get(id=pk)
    libro.delete()
    return redirect('/biblioteca/')

