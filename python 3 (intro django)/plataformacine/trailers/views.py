from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request,'trailers/index.html')

def nuevoTrailerView(request):
    return render(request,'trailers/nuevo.html')