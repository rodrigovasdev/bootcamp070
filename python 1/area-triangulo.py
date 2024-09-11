import math

def validarNumeros(a,b,c):
    if (a < 0 or b < 0 or c < 0):
        return False
    else:
        return True

def validarTriangulo(lado1,lado2,lado3):
    if (lado1 + lado2) < lado3 or (lado1 + lado3) < lado2 or (lado2 + lado3) < lado1:
        return False
    else:
        return True
    
def calcularSemiperimetro(lado1,lado2,lado3):
    s = (lado1 + lado2 + lado3) / 2
    return s


def calcular_area_triangulo(lado1,lado2,lado3):
    if validarNumeros(lado1,lado2,lado3):
        if validarTriangulo(lado1,lado2,lado3):
            s = calcularSemiperimetro(lado1,lado2,lado3)
            area = s * (s - lado1) * (s - lado2) * (s - lado3)
            area = math.sqrt(area)
            return ('El valor del area es: ',area,'CM2 !')
        else:
            return ('Triangulo invalido !')
    else:
        return ('Sus medidas deben ser numeros positivos !')
    
print(calcular_area_triangulo(3,4,5))

