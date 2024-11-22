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