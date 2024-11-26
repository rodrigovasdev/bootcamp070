from django.shortcuts import render



def evaluar_palindromo(palabra):
    # Eliminar espacios y convertir a minúsculas para una evaluación consistente
    palabra_procesada = palabra.replace(" ", "").lower()
    # Verificar si es un palíndromo
    es_palindromo = palabra_procesada == palabra_procesada[::-1]
    # Crear el diccionario con el resultado
    resultado = {
        'palabra': palabra,
        'palindromo': 'es palindromo' if es_palindromo else 'no es palindromo'
    }
    return resultado
# Create your views here.
def PalindromoView(request,palabra):
    context = evaluar_palindromo(palabra)
    return render(request,'palindromo.html',context)

def PalindromoIndexView(request):
    return render(request,'index.html')
