'''
Dada la siguiente lista, debes escribir un programa que analice si una persona es Villano o Heroe, 
Tu programa debe crear una nueva lista con la frase
"Pepito es un Villano, su super poder es Mirar con los ojos cerrados y habita en Santiago" O
"Pepito es un Heroe, su super poder es Volar y habita en Valparaiso" Segun corresponda
En el caso de que la persona sea Villano y Heroe a la vez (Osea su clave "villano" y "heroe" son True ambas dos)
debes imprimir el mensaje
"Pepito el contradictorio Villano/Heroe, su super poder AQUI-DEBE-IR-EL-SUPERPODER y habita en AQUI-DEBE-IR-CIUDAD"
Para este programa debes definir al menos dos funciones 
'''

lista = [
    {"nombre": "Carlos", "villano": False, "heroe": True, "superpoder": "Invisibilidad", "ciudad": "Ciudad Gótica"},
    {"nombre": "Luis", "villano": True, "heroe": False, "superpoder": "Super Velocidad", "ciudad": "Buenos Aires"},
    {"nombre": "Ana", "villano": False, "heroe": True, "superpoder": "Teletransportación", "ciudad": "Tokio"},
    {"nombre": "Marta", "villano": True, "heroe": True, "superpoder": "Control Mental", "ciudad": "París"},
    {"nombre": "Pedro", "villano": False, "heroe": True, "superpoder": "Fuerza Sobrehumana", "ciudad": "Nueva York"},
    {"nombre": "Clara", "villano": True, "heroe": False, "superpoder": "Manipulación del Tiempo", "ciudad": "Londres"},
    {"nombre": "Juan", "villano": True, "heroe": True, "superpoder": "Vuelo", "ciudad": "Los Ángeles"},
]

def listaHeroesVillanos(personajes):
    nuevaLista = []
    for personaje in personajes:
        if personaje['villano'] and personaje['heroe']:
            nuevoContradictorio = personaje['nombre'] + ' el contradictorio Villano/Heroe, su super poder es ' + personaje['superpoder'] + ' Y  habita en ' + personaje['ciudad']
            nuevaLista.append(nuevoContradictorio)
        elif personaje ['villano']:
            nuevoVillano =  personaje['nombre'] + ' es un Villano, su super poder es ' + personaje['superpoder'] + ' Y  habita en ' + personaje['ciudad']
            nuevaLista.append(nuevoVillano)
        elif personaje['heroe']:
            nuevoHeroe =  personaje['nombre'] + ' es un Heroe, su super poder es ' + personaje['superpoder'] + ' Y  habita en ' + personaje['ciudad']
            nuevaLista.append(nuevoHeroe)
    return nuevaLista

def mostrarLista(lista):
    for elemento in lista:
        print(elemento)

heroesvillanos = listaHeroesVillanos(lista)
mostrarLista(heroesvillanos)
