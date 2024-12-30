from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def agregar(request):
    return render(request,'postForm.html',{})

def agregarregistro(request):
    titulo = request.POST['title']
    contenido = request.POST['content']
    autor = request.POST['author']
    post = Post(title=titulo, content=contenido, author=autor)
    post.save()
    return redirect('/blogsite/tablitafeliz')