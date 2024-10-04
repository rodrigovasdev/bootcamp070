class Vehiculo():
    def __init__(self, modelo, marca, color, nro_puertas, kilometraje):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.nro_puertas = nro_puertas
        self.kilometraje = kilometraje
        self.velocidad = 0
        self.encendido = False


    ruedas=4
    #SET
    def set_modelo(self,modelito):
        self.modelo = modelito

    def set_color(self, color):
        self.color = color

    #GET
    def get_modelo(self):
        return self.modelo
    
    def get_marca(self):
        return self.marca

    def get_color(self):
        return self.color   
 

    
    def desplazamiento(self):
        print("El vehículo se está desplazando sobre 4 ruedas")

miAutito = Vehiculo('Miata','Mazda','Negro',2,20000)

print("Mi", miAutito.get_marca(), miAutito.get_modelo(), "es",miAutito.get_color())
miAutito.set_color('Celeste')
miAutito.set_modelo('RX-7')
print("Mi", miAutito.get_marca(), miAutito.get_modelo(), "es",miAutito.get_color())
print('Cantida de ruedas',miAutito.ruedas)
print(Vehiculo.__name__)