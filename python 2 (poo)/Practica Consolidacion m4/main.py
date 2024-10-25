from clases import Vehiculo,Automovil,Particular,Carga,Bicicleta,Motocicleta


""" 
Parte 1 (Repetir 3 veces...):

nuevaMarca = input('Ingrese marca ')
nuevoModelo = input('Ingrese modelo ')
nroRuedas = input('Ingrese numero de ruedas ')
nuevaVelocidad = int(input('Ingrese velocidad '))
nuevaCilindrada = int(input('Ingrese cilindrada '))
auto1 = Automovil(nuevaMarca,nuevoModelo,nroRuedas,nuevaVelocidad,nuevaCilindrada)

"""

#Parte 2!
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print('Particular: ',particular)
print('Carga: ',carga)
print('Bicicleta: ', bicicleta)
print('Motocicleta: ',motocicleta)

print('Motocicleta es instancia con relacion a Vehiculo: ',isinstance(motocicleta,Vehiculo))
print('Motocicleta es instancia con relacion a Automovil: ',isinstance(motocicleta,Automovil))
print('Motocicleta es instancia con relacion a Particular: ',isinstance(motocicleta,Particular))
print('Motocicleta es instancia con relacion a Carga: ',isinstance(motocicleta,Carga))
print('Motocicleta es instancia con relacion a Bicicleta: ',isinstance(motocicleta,Bicicleta))
print('Motocicleta es instancia con relacion a Motocicleta: ',isinstance(motocicleta,Motocicleta))

#Parte 3
motocicleta.guardar_datos_csv()
motocicleta.leer_datos_csv()


