from django.shortcuts import render, redirect
from .forms import LibroForm
from .models import LibroModel
from django.views.generic import TemplateView, ListView
# Create your views here.
def new_libro_view(request):
    context ={}
    # crear el objeto form
    form = LibroForm(request.POST or None, request.FILES or None)
    # verificar si el formulario es valido
    if form.is_valid():
        # guardar los datos del formulario al modelo
        form.save()
        return redirect('/')
    context = {'formulariogato' : form}
    return render(request, "formulario.html", context)

class BookListView(ListView):
    template_name = 'lista_libros.html'
    model= LibroModel
    context_object_name = 'list_book'
