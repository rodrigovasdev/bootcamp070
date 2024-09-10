def areaRectangulo(base, altura):
    if (base < 0 or altura < 0):
        mensajeError = 'Sus parametros deben ser positivos !'
        return mensajeError
    else:
        area = base * altura
        return area

base = input('Ingrese la base de su rectangulo')
altura = input('Ingrese la altura de su rectangulo')
base = int(base)
altura = int(altura)

area = areaRectangulo(base,altura)
print(area)