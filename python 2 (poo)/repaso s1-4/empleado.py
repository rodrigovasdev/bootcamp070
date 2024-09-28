"""
Una empresa te pide que programes su sistema de pagos, por el momento debes definir las clases
para un Desarrollador, Gerente, y Freelance sabiendo que, estos tres comparten caracteristicas como:
nombre, apellido, id. Debes programar un metodo calcular_pago que calcule el salario de cada uno de 
estas clases. Teniendo en cuenta que, El desarrollador tiene un salario base, El freelance gana por horas trabajadas
(horas_trabajadas X tarifa_por_hora) y el gerente tiene un salario base mas bonos.

Programa las clases y sus metodos correspondientes, empleando polimorfismo y herencia.
"""

class Empleado():
    #Metodo Constructor
    def __init__(self,nombre,apellido,id) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
    
    #Declarar metodo polimorfico
    def calcular_pago(self):
        pass

class Desarrollador(Empleado):
    #Metodo Constructor
    def __init__(self, nombre, apellido, id, salarioBase) -> None:
        super().__init__(nombre, apellido, id)
        self.salario_base = salarioBase

    def calcular_pago(self):
        print(f'El salario del desarrollador es: {self.salario_base}')

class Freelance(Empleado):
    #Metodo Constructor
    def __init__(self, nombre, apellido, id,horas_trabajadas, tarifa_por_hora ) -> None:
        super().__init__(nombre, apellido, id)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_pago(self):
        salario = self.horas_trabajadas * self.tarifa_por_hora
        print(f'El salario del freelance es: {salario}')

class Gerente(Empleado):
    #Metodo Constructor
    def __init__(self, nombre, apellido, id, salarioBase, bono) -> None:
        super().__init__(nombre, apellido, id)
        self.salario_base = salarioBase
        self.bono = bono
    
    def calcular_pago(self):
        salario = self.salario_base + self.bono
        print(f'El salario del gerente es: {salario}')


#Instancia de clases
desarrolladorcito = Desarrollador('Rodrigo','Vasquez',1,12000)
freenlancito = Freelance('Rodrigo','Morales',2,500,7000)
gerentito = Gerente('Rodrigo','Perez',3,30000, 10)

desarrolladorcito.calcular_pago()
freenlancito.calcular_pago()
gerentito.calcular_pago()


        