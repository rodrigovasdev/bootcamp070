"""
De la siguiente lista de estudiantes, tienes que definir una funcion que evalue en cual materia tuvieron mejor rendimiento
es decir, los estudiantes en promedio obtuvieron mejores notas, Finalmente imprime la asignatura y el promedio de 
los estudiantes en dicha asignatura
"""

estudiantes = [
    {"nombre": "Carlos", "matematicas": 85, "ciencias": 90, "historia": 88},
    {"nombre": "Ana", "matematicas": 92, "ciencias": 81, "historia": 85},
    {"nombre": "Luis", "matematicas": 78, "ciencias": 75, "historia": 80},
    {"nombre": "Maria", "matematicas": 95, "ciencias": 100, "historia": 98},
    {"nombre": "Juan", "matematicas": 65, "ciencias": 70, "historia": 60},
]

def mejorPromedio(notasMate, notasCiencia, notasHist):
    if notasMate > notasCiencia and notasMate > notasHist:
        return ("El mejor promedio es de matematicas: ", notasMate)
    elif notasCiencia > notasHist:
        return ("El mejor promedio es de ciencias: ", notasCiencia)
    else:
        return ("El mejor promedio es de historia: ", notasHist)

def mejorAsignatura(estudiantes):
    notasMate = 0
    notasCiencia = 0
    notasHist = 0
    for estudiante in estudiantes:
        notasMate = notasMate + estudiante['matematicas']
        notasCiencia = notasCiencia + estudiante['ciencias']
        notasHist = notasHist + estudiante['historia']
    totalNotas = len(estudiantes)
    notasMate = notasMate / totalNotas
    notasCiencia = notasCiencia / totalNotas
    notasHist = notasHist / totalNotas
    mensaje = mejorPromedio(notasMate,notasCiencia,notasHist)
    print(mensaje)

mejorAsignatura(estudiantes)
