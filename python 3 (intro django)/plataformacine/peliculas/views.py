from django.shortcuts import render, redirect
from .forms import PeliculaForm
# Create your views here.
def nuevaPeliculaView(request):
    return render(request,'peliculas/nueva.html')

def indexView(request):
    return render(request,'peliculas/index.html')

def peliculaform_view(request):
    # crear el objeto form
    form = PeliculaForm(request.POST or None, request.FILES or None)
    # verificar si el formulario es valido
    if form.is_valid():
        # guardar los datos del formulario al modelo
        form.save()
        return redirect('/')
    context= {'formulario' : form}
    return render(request, "datosform.html", context)
