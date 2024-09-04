estudiantes = [
 {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
 {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
 {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
 {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
 {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

def calcularPromedio(notas):
    sumaNotas = 0
    for nota in notas:
        sumaNotas +=  nota
    promedio = sumaNotas / len(notas)
    return promedio

def esPrimo(numero):
    divisores = 0
    for i in range(1,numero):
        if numero % i == 0:
            divisores += 1
    if divisores == 1:
        return True
    else:
        return False

for estudiante in estudiantes:
    promedio = calcularPromedio(estudiante['calificaciones'])
    if estudiante['edad'] > 18 and promedio > 85:
        print('Estudiante: ',estudiante['nombre'],'Promedio de calificaciones: ',promedio)

    if estudiante['edad'] > 18 and esPrimo(estudiante['edad']):
       print('El promedio de ',estudiante['nombre'],'es ',promedio)

