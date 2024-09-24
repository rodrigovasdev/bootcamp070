"""
Dada la siguiente lista de palabras, tienes que evaluar cuales de ellas son
palabras magicas, para que una palabra sea magica tiene que cumplir al menos 1 de las 
siguientes 3 condiciones escenciales:
1 Contiene todas las vocales (a, e, i, o, u).
2 Tiene más de 7 letras.
3 Contiene tanto una 'a' como una 'z'.

Finalmente imprime una lista con las palabras magicas
"""


palabras = [
    "zorro", "fantasia", "astronauta", "computadora", "relampago",
    "cazador", "amortiguador", "jazmin", "espectacular", "almohada",
    "azucar", "bazar", "pizzero", "camion", "travesia", 
    "razonable", "calabaza", "atrapazombis", "hazaña", "constelacion"
]

def tieneTodasVocales(palabra):
    if 'a' in palabra and 'e' in palabra and 'i' in palabra and 'o' in palabra and 'u' in palabra: 
        return True
    else:
        return False
    
def tieneAZ(palabra):
    if 'a' in palabra and 'z' in palabra:
        return True
    else:
        return False

def tieneMas7Caracteres(palabra):
    if len(palabra) > 7:
        return True
    else:
        return False


def filtraPalabrasMagicas(palabras):
    palabrasMagicas = []
    for palabra in palabras:
        if tieneTodasVocales(palabra) or len(palabra) > 7 or tieneAZ(palabra):
            palabrasMagicas.append(palabra)
    return palabrasMagicas



listaDePalabrasMagicas = filtraPalabrasMagicas(palabras)
print('A continuacion las palabras magicas: ')
for elemento in listaDePalabrasMagicas:
    print(elemento)