from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("Mensaje, Hola Mundo. cualquier cosa")

class IndexPageView(TemplateView):
    template_name = "index.html"
