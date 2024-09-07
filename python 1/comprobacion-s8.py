#Eliminar elementos repetidos de la lista
#Ordenar la lista en orden ascendente

lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
set = set(lista) #Eliminamos valores repetidos
lista = list(set)

print('Lista inicial')
print(lista)
largoLista = len(lista)
for i in range(0,largoLista):
    for j in range(i+1,largoLista):
        if lista[i] > lista[j]:
            varTemporal = lista[i]
            lista[i] = lista[j]
            lista[j] = varTemporal
print('Lista ordenada')
print(lista)  