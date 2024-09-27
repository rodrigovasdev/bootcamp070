class Persona:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
    
    def movimiento(self):
        print("Caminando")

class Maratonista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def movimiento(self):
        print('Trotando')

class Ciclista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    
    def movimiento(self):
        print('Rodando')

persona1 = Persona('Rodrigo')
maratonista1 = Maratonista('Rodrigo Maratonista')
ciclista1 = Ciclista('Rodrigo el Ciclista')

persona1.movimiento()
maratonista1.movimiento()
ciclista1.movimiento()