"""
Dada la siguiente super clase Calculadora, debes crear las clases hijas Sumar, Resta, Multiplicar y Dividir
Debes definir el metodo calcular para cada una de estas clases y actuar con polimorfismo y herencia.
El metodo calcular() debe mostrar por pantalla el resultado de la operacion asignada.

Recuerda validar la division. No se puede dividir por 0
"""

class Calculadora:
    #Metodo constructor que es HEREDADO a las demas clases hijas.
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calcular(self):
        pass

class Suma(Calculadora):

    def calcular(self):
        suma = self.a + self.b
        print(f'La suma entre {self.a} y {self.b} es: {suma}')

class Resta(Calculadora):

    def calcular(self):
        resta = self.a - self.b
        print(f'La resta entre {self.a} y {self.b} es: {resta}')

class Multiplicacion(Calculadora):

    def calcular(self):
        producto = self.a * self.b
        print(f'El producto entre {self.a} y {self.b} es: {producto}')

class Division(Calculadora):

    def calcular(self):  
        if self.b == 0:
            print ('Fatal error: No se puede dividir por 0 !!')
        else:
            cuociente = self.a / self.b
            resto = self.a % self.b
            print(f'El cuociente entre {self.a} y {self.b} es: {cuociente} y su resto es {resto}')

sumita = Suma(10,2)
sumita.calcular()

restita = Resta(9,8)
restita.calcular()

multiplicacioncita = Multiplicacion(9,0)
multiplicacioncita.calcular()

divisioncita = Division(81,3)
divisioncita.calcular()

    
        