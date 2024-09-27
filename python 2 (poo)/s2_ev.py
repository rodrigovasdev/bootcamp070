class Persona():
    #Metodo constructor
    def __init__(self,nombre,apellido,sexo,edad,estatura,peso):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def __str__(self):
        return (f"Persona: {self.nombre} {self.apellido} y su edad es {self.edad}")
        
    #Getters
    def get_nombre(self):
        return (self.nombre)
    def get_apellido(self):
        return (self.apellido)
    def get_sexo(self):
        return (self.sexo)
    def get_edad(self):
        return (self.edad)
    def get_estatura(self):
        return (self.estatura)
    def get_peso(self):
        return (self.peso)
    
    #Setters
    def set_nombre(self,nombreNuevo):
        self.nombre = nombreNuevo
    def set_apellido(self,apellidoNuevo):
        self.apellido = apellidoNuevo
    def set_sexo(self,sexoNuevo):
        self.sexo = sexoNuevo
    def set_edad(self,edadNueva):
        self.edad = edadNueva
    def set_estatura(self,estaturaNueva):
        self.estatura = estaturaNueva
    def set_peso(self,pesoNuevo):
        self.peso = pesoNuevo

persona_1 = Persona('Pedro','Vivas','Masculino',20,1.78,68)
persona_2 = Persona('Juan','Camargo','Masculino',18,1.8,75)

print(persona_1)
print(persona_2)

persona_1.set_edad(21)
persona_2.set_apellido('Santiago')

print(persona_1)
print(persona_2)