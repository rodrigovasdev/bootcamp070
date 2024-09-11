personas = [
    {"nombre": "Carlos", "edad": 17},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Ana", "edad": 15},
    {"nombre": "Marta", "edad": 18},
    {"nombre": "Sofía", "edad": 19}
]



def clasificar_personas(personas):
    lista = []
    for persona in personas:        
        if persona['edad'] > 18:
            mensaje = persona['nombre'] + ' Es mayor de edad'
            lista.append(mensaje)
        else:
            mensaje = persona['nombre'] + ' Es menor de edad'
            lista.append(mensaje)
    return lista

personasClasificadas = clasificar_personas(personas)
print(personasClasificadas)


"""
Crea una función llamada clasificar_personas(lista) que reciba la lista de personas y genere o retorne una nueva lista en la que,
para cada persona, se incluya su nombre junto con el mensaje "es mayor de edad"
o "es menor de edad", dependiendo de su edad.

Finalmente imprime esta nueva lista por consola.
"""