class NuestraExcepcioncita(Exception):
    def __init__(self, mensaje) -> None:
        super().__init__(mensaje)

class NumeroFormatoExcepcion(Exception):
    def __init__(self, value):
        message = f'{value} no es un número'
        super().__init__(message)

def division_entera(x,y):

    if y == 0:
        raise NuestraExcepcioncita('')
    elif type(x) != int:
        raise NumeroFormatoExcepcion(x)
    elif type(y) != int:
        raise NumeroFormatoExcepcion(y)
    else:
        return x/y



try:
    numerito = division_entera(10,'asdsa')
    print(numerito)
except NuestraExcepcioncita:
    print('No c puede dividir por 0')

