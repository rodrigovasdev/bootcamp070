import csv

class Vehiculo():
    def __init__(self,marca,modelo,nro_ruedas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self) -> str:
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, Numero Ruedas: {self.nro_ruedas}')
    
    def guardar_datos_csv(self):
        try:
            archivo = open('vehiculos.csv', "w")
            datos = [(self.__class__, self.__dict__)]
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerows(datos)
            archivo.close()
        except FileExistsError:
            print('No se encontro el archivo')
        except:
            print('Se produjo un error')
    
    def leer_datos_csv(self):
        try:
            vehiculos = []
            archivo = open('vehiculos.csv', "r")
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv:
                claseVehiculo = str(self.__class__)
                if claseVehiculo in vehiculo:
                    vehiculos.append(vehiculo)
            archivo.close()
            print ('Lista de vehiculos: \n',vehiculos)
        except FileExistsError:
            print('No se encontro el archivo')
        except:
            print('Se produjo un error')

    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo) -> None:
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self) -> str:
        return (super().__str__() + f', Tipo: {self.tipo}')

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor) -> None:
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self) -> str:
        return (super().__str__() + f', Numero radios: {self.nro_radios}, Cuadro: {self.cuadro}, Motor: {self.motor} ')

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada) -> None:
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) -> str:
        return (super().__str__() + f', Velocidad: {self.velocidad}, Cilindrada: {self.cilindrada}')

class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos) -> None:
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos
    
    def __str__(self) -> str:
        return (super().__str__() + f', Numero de puestos: {self.nro_puestos}')

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga) -> None:
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self) -> str:
        return (super().__str__() + f', Carga: {self.carga}')