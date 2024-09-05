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

# Funcion que recibe una lista de numeros y retorna su promedio.
# Usada para retornar el promedio de goles y de edad de los MD
def obtenerPromedioGoles(listaGoles):
    sumaGoles = 0
    for goles in listaGoles:
        sumaGoles = sumaGoles + goles
    promedioGoles = sumaGoles / len(listaGoles)
    return promedioGoles


# Funcion que recibe una lista de numeros y retorna una sumatoria de los valores de la lista
def obtenerTotalGoles(listaGoles):
    sumaGoles = 0
    for goles in listaGoles:
        sumaGoles =  sumaGoles + goles
    return sumaGoles

# Funcion que muestra los Jugadores poderosos: Jugadores con mas de 20 partidos jugados
# Y un promedio por sobre 10 goles
def mostrarJugadoresPoderosos():
    jugadoresPoderosos = []
    for jugador in jugadores:
        promedioGoles = obtenerPromedioGoles(jugador['goles'])
        if jugador['partidos_jugados'] > 20 and promedioGoles > 10:
            jugadoresPoderosos.append(jugador['nombre'])
    print('A continuacion los jugadores poderosos: ')
    print(jugadoresPoderosos)


# Funcion que muestra los delanteros infalibles: Jugadores que son delanteros, cuentan con mas de 20 partidos jugados
# Y tienen mas de 25 a;os
def mostrarDelanterosInfalibles():
    delanterosInfalibles = []
    for jugador in jugadores:
        promedioGoles = obtenerPromedioGoles(jugador['goles'])
        if jugador['partidos_jugados'] > 20 and jugador['posicion'] == 'Delantero' and jugador['edad'] > 25:
            nuevoDelanteroInfalible = {'nombre':jugador['nombre'],'goles':promedioGoles}
            delanterosInfalibles.append(nuevoDelanteroInfalible)
    print('A continuacion los delanteros infalibles: ')
    print(delanterosInfalibles)



#  Identifica al defensa con más goles.
def mostrarDefensaGoleador():
    maximoGoles = 0
    for jugador in jugadores:
        golesJugador = obtenerTotalGoles(jugador['goles'])
        if jugador['posicion'] == 'Defensa' and golesJugador > maximoGoles:
            defensaGoleador = jugador
            maximoGoles = golesJugador
    print('Defensa con mas goles: ',defensaGoleador,'Goles: ',maximoGoles)




# Encuentra al jugador con el mejor promedio de goles por partido jugado. @Jugador Estrella
def calcularPtjEstrella(promedioGoles,cantidadPartidosJugados):
    puntajeEstrellita = promedioGoles / cantidadPartidosJugados
    return puntajeEstrellita

def mostrarJugadorEstrella():
    recordPtjEstrella = 0
    for jugador in jugadores:
        promedioGoles = obtenerPromedioGoles(jugador['goles'])
        puntajeEstrella = calcularPtjEstrella(promedioGoles,jugador['partidos_jugados'])
        if puntajeEstrella > recordPtjEstrella:
            jugadorEstrella = jugador
            recordPtjEstrella = puntajeEstrella
    print('El jugador estrella es: ',jugadorEstrella['nombre'],'Con un puntaje estrella de: ',recordPtjEstrella)


# Calcula la edad promedio de los mediocampistas.
def mostrarEdadPromedioMD():
    edades = []
    for jugador in jugadores:
        if jugador['posicion'] == 'Mediocampista':
            edades.append(jugador['edad'])
    promedioEdades = obtenerPromedioGoles(edades)
    print('La edad promedio de los mediocampistas es: ',promedioEdades)


# 1. Funcion que muestra todos los jugadores de la lista
# 2. Mostrar jugadores por posicion
# 3. Agrega jugadores a la lista
    
menu = True
while (menu):
    opcion = input('1.- Mostrar jugadores poderosos \n 2.- Mostrar delanteros infalibles \n 3.- Mostrar defensa goleador \n 4.- Mostrar jugador estrella \n 5.- Mostrar edad promedio mediocampistas \n 6.- Salir \n Ingrese su opcion: ')
    opcion = int(opcion)
    if opcion == 1:
        mostrarJugadoresPoderosos()
    elif opcion == 2: 
        mostrarDelanterosInfalibles()
    elif opcion == 3: 
        mostrarDefensaGoleador()
    elif opcion == 4: 
        mostrarJugadorEstrella()
    elif opcion == 5: 
        mostrarEdadPromedioMD()
    elif opcion == 6: 
        print('Muchas gracias por visitar nuestra BD de jugadores')
        menu = False


