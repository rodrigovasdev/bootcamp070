from django.shortcuts import render, redirect
from .models import Sala, Reserva
from .forms import SalaForm, ReservaForm
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

def lista_reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'lista_reservas.html',context)

def nueva_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reservas')
    else:
        form = ReservaForm()
        context = {'form': form}
    return render(request, 'nueva_reserva.html',context)

def editar_reserva(request,id):
    reserva = Reserva.objects.get(id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('/reservas')
    else:
        form = ReservaForm(instance=reserva)
        context = {'form': form}
    return render(request, 'editar_reserva.html',context)