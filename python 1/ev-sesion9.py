def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return ('El divisor no puede ser 0 !!!!')
    else:
        return a / b
    
def operaciones(a,b):
    tupla = (suma(a,b),resta(a,b),multiplicacion(a,b),division(a,b))
    return tupla

a = input('Ingrese un numero')
b = input('Ingrese otro numero')
a = float(a)
b = float(b)
resultados = operaciones(a,b)
diccionario = {'Suma':resultados[0],'Resta':resultados[1],'Multiplicacion':resultados[2],'Division':resultados[3]}
print(diccionario)
