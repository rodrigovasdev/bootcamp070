from django.shortcuts import render, redirect
from .models import Sala, Reserva
from .forms import SalaForm
# Create your views here.
def lista_salas(request):
    salas = Sala.objects.all()
    context = {'salas': salas}
    return render(request, 'lista_salas.html',context)

def detalle_sala(request,id):
    sala = Sala.objects.get(id=id)
    context = {'sala': sala}
    return render(request, 'sala_detalle.html',context)


def registrar_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('/salas')  # Redirige a otra vista después de guardar
    else:
        form = SalaForm()
        context = {'form': form}
    return render(request, 'registrar_sala.html',context)

def editar_sala(request,id):
    sala = Sala.objects.get(id=id)
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('/salas')
    else:
        form = SalaForm(instance=sala)
        context = {'form': form}
    return render(request, 'editar_sala.html',context)

def eliminar_sala(request,id):
    sala = Sala.objects.get(id=id)
    sala.delete()
    return redirect('/salas')