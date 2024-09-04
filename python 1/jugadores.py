# Con la siguiente lista de diccionarios de jugadores de un equipo de fútbol,
# filtra y muestra únicamente los jugadores que han jugado más de
# 20 partidos y cuyo promedio de goles sea superior a 10. Jugadores Poderosos

# Además:
# Calcula el promedio de goles de los jugadores que tienen más de
# 20 partidos jugados, cuya posición en el campo sea "Delantero"
# y cuya edad sea superior a 25 años. Delanteros Infalibles

jugadores = [
    {'nombre': 'Lionel', 'edad': 33, 'posicion': 'Delantero', 'partidos_jugados': 30, 'goles': [15, 12, 18]},
    {'nombre': 'Sergio', 'edad': 28, 'posicion': 'Defensa', 'partidos_jugados': 25, 'goles': [2, 1, 0]},
    {'nombre': 'Andrés', 'edad': 24, 'posicion': 'Mediocampista', 'partidos_jugados': 22, 'goles': [6, 5, 8]},
    {'nombre': 'Karim', 'edad': 31, 'posicion': 'Delantero', 'partidos_jugados': 28, 'goles': [14, 11, 13]},
    {'nombre': 'Gerard', 'edad': 34, 'posicion': 'Defensa', 'partidos_jugados': 32, 'goles': [3, 4, 2]},
    {'nombre': 'Cristiano', 'edad': 36, 'posicion': 'Delantero', 'partidos_jugados': 33, 'goles': [18, 17, 20]},
    {'nombre': 'Neymar', 'edad': 29, 'posicion': 'Delantero', 'partidos_jugados': 26, 'goles': [15, 14, 12]},
    {'nombre': 'Modric', 'edad': 35, 'posicion': 'Mediocampista', 'partidos_jugados': 29, 'goles': [4, 3, 5]},
    {'nombre': 'Vinicius', 'edad': 21, 'posicion': 'Delantero', 'partidos_jugados': 27, 'goles': [12, 13, 14]},
    {'nombre': 'Ramos', 'edad': 34, 'posicion': 'Defensa', 'partidos_jugados': 28, 'goles': [7, 6, 8]},
    {'nombre': 'Piqué', 'edad': 33, 'posicion': 'Defensa', 'partidos_jugados': 31, 'goles': [3, 4, 5]},
    {'nombre': 'Kroos', 'edad': 30, 'posicion': 'Mediocampista', 'partidos_jugados': 30, 'goles': [6, 5, 4]},
    {'nombre': 'Alba', 'edad': 32, 'posicion': 'Defensa', 'partidos_jugados': 27, 'goles': [1, 2, 3]},
]

# 1. Identifica al defensa con más goles.
# 2. Encuentra al jugador con el mejor promedio de goles por partido jugado. @Jugador Estrella
# 3. Calcula la edad promedio de los mediocampistas.

def obtenerPromedioGoles(listaGoles):
    sumaGoles = 0
    for goles in listaGoles:
        sumaGoles = sumaGoles + goles
    promedioGoles = sumaGoles / len(listaGoles)
    return promedioGoles

def obtenerTotalGoles(listaGoles):
    sumaGoles = 0
    for goles in listaGoles:
        sumaGoles =  sumaGoles + goles
    return sumaGoles


jugadoresPoderosos = []
def mostrarJugadoresPoderosos():
    for jugador in jugadores:
        promedioGoles = obtenerPromedioGoles(jugador['goles'])
        if jugador['partidos_jugados'] > 20 and promedioGoles > 10:
            jugadoresPoderosos.append(jugador['nombre'])
    print('A continuacion los jugadores poderosos: ')
    print(jugadoresPoderosos)

delanterosInfalibles = []
def mostrarDelanterosInfalibles():
    for jugador in jugadores:
        promedioGoles = obtenerPromedioGoles(jugador['goles'])
        if jugador['partidos_jugados'] > 20 and jugador['posicion'] == 'Delantero' and jugador['edad'] > 25:
            nuevoDelanteroInfalible = {'nombre':jugador['nombre'],'goles':promedioGoles}
            delanterosInfalibles.append(nuevoDelanteroInfalible)
    print('A continuacion los delanteros infalibles: ')
    print(delanterosInfalibles)


def mostrarDefensaGoleador():
    maximoGoles = 0
    for jugador in jugadores:
        golesJugador = obtenerTotalGoles(jugador['goles'])
        if jugador['posicion'] == 'Defensa' and golesJugador > maximoGoles:
            defensaGoleador = jugador
            maximoGoles = golesJugador
    print('Defensa con mas goles: ',defensaGoleador,'Goles: ',maximoGoles)


mostrarJugadoresPoderosos()
mostrarDelanterosInfalibles()
mostrarDefensaGoleador()