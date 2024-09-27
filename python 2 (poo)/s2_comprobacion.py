
# Definiendo la clase Animal()
class Animal():
    # Metodo constructor. Se llama a este metodo cada vez 
    # Se crea un nuevo objeto de tipo Animal()
    def __init__(self,nombre,raza,edad,peso): 
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def __str__(self) :
        return (f"Nombre: {self.nombre} y su edad es {self.edad}. Su raza es {self.raza}. Su peso es {self.peso}")



# Creamos los objetos Animal() || Creamos nuevas instancias de la clase Animal()
caballito = Animal('Zeus','Pura Sangre',5,450)
leoncito = Animal('Boulder','Atlas',10,130)


print ('Mi animal es un:',caballito.raza,'Y su nombre es ',caballito.nombre)
print ('Mi animal es un:',leoncito.raza,'Y su nombre es ',leoncito.nombre)
print(leoncito)

        