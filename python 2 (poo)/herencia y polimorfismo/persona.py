class Persona:
    #Metodo constructor
    def __init__(self, nombre, apellidos, cedula):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula

    def get_tipo(self):
        a = 2 - 9 
        print('Soy de la clase Persona!', a)

    #APLICANDO POLIMORFISMO
    def imprimir_datos(self):
        print(f'Nombre: {self.nombre} \nApellidos: {self.apellidos}\nCédula: {self.cedula} Datos mostrados desde Imprimir_Datos')

    def __str__(self):
        return (f'Nombre: {self.nombre} \nApellidos: {self.apellidos}\nCédula: {self.cedula} Datos mostrados desde funcion STR')
    
class Supervisor(Persona):
    #Metodo constructor
    def __init__(self, nombre, apellidos, cedula, zona):
        super().__init__(nombre, apellidos, cedula)
        self.zona = zona

    def get_tipo(self):
        a = 100 + 12
        print('Soy de la clase Supervisor!', a)

    #APLICANDO POLIMORFISMO
    def imprimir_datos(self):
        super().imprimir_datos()
        print(f'Zona: {self.zona}')
    
    def __str__(self):
        datos = super().__str__ + (f'\nZona: {self.zona}')
        return datos
    
class Cliente(Persona):
    #Metodo constructor
    def __init__(self, nombre, apellidos, cedula, descuento):
        super().__init__(nombre, apellidos, cedula)
        self.descuento = descuento
    
    def get_tipo(self):
        a = 2 + 3
        print('Soy de la clase Cliente!', a)
    
    #APLICANDO POLIMORFISMO
    def imprimir_datos(self):
        super().imprimir_datos()
        print(f'Descuento: {self.descuento}')

    def __str__(self):
        datos = super().__str__ + (f'\nDescuento: {self.descuento}')
        return datos
    