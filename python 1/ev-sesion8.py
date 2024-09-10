mi_lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
for sublista in mi_lista:
    if sublista[0] == 0:
        continue
    listaFiltrada = []
    for numero in sublista:
        if numero == 0:
            continue
        listaFiltrada.append(numero)
    print(listaFiltrada)

diccionario = {'A':mi_lista[0],'B':mi_lista[1],'C':mi_lista[2],'D':mi_lista[3]}
print(diccionario)