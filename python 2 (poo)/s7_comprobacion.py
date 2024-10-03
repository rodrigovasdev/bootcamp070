
"""
#Funcion Recursiva!
def obtener_edad():
    try:
        edad = int(input('Ingrese su edad: '))
        return edad
    except ValueError:
        print('Ingresa un numero entero !')
        return obtener_edad()

"""

def obtener_edad():
    while True:
        try:
            edad = int(input('Ingrese su edad: '))
            return edad
        except ValueError:
            print('Debes ingresar un numero entero !')

edad = obtener_edad()

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')