from django.shortcuts import render
from .forms import BoardsForm
from django.http import HttpResponseRedirect
# Create your views here.
def boardsform_view(request):
    context ={}
    # crear el objeto form
    form = BoardsForm(request.POST or None, request.FILES or None)
    # verificar si el formulario es valido
    if form.is_valid():
        # guardar los datos del formulario al modelo
        form.save()
        return HttpResponseRedirect('/')
    context = {'formulariogato' : form}
    return render(request, "formulario.html", context)

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
