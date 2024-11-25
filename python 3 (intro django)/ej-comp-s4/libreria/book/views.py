import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    return HttpResponse('Mensaje de book')

class IndexView(TemplateView):
    template_name = 'index.html'

class PepitoView(TemplateView):
    template_name = 'pepito.html'

def obtenerFecha(request,name):
    fechaActual = datetime.datetime.now()
    context = {'fecha' : fechaActual, 'nombre' : name}
    return render(request, 'fecha.html', context)