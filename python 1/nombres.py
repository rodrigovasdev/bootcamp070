# Con la siguiente lista de nombres
# Debes añadir un "Hola" antes de cada nombre
# Luego imprimir la lista por consola
nombres = ["Carlos", "Luis", "Ana", "Marta", "Sofía"]

largoLista = len(nombres)
for indice in range(largoLista):
    print('Para ',nombres[indice])
    apellido = input("Ingrese el apellido ")
    nombres[indice] = nombres[indice] + ' ' + apellido
print(nombres)

"""
Dada una lista de nombres tienes que pedirle al usuario que ingrese un apellido para cada nombre mientras se ejecuta el programa
Luego imprimir esa lista de nombres actualizada con los apellidos
"""