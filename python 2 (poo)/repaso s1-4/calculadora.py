"""
Dada la siguiente super clase Calculadora, debes crear las clases hijas Sumar, Resta, Multiplicar y Dividir
Debes definir el metodo calcular para cada una de estas clases y actuar con polimorfismo y herencia.
El metodo calcular() debe mostrar por pantalla el resultado de la operacion asignada.

Recuerda validar la division. No se puede dividir por 0
"""

class Calculadora:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calcular(self):
        pass
        