
def division_entera(x,y):
    if y == 0:
        raise ZeroDivisionError('No se puede dividir por cero')
    try:
        dividendo = int(x)
        divisor = int(y)
        return dividendo/divisor
    except ZeroDivisionError:
        print('No se puede dividir por cero!!!')
    except ValueError:
        print('Debes ingresar numeros enteros')
    except Exception as error:
        print('Se ha generado un error no previsto',type(error).__name__)

resultado = division_entera(1, 0)
print(resultado)