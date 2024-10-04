class RangoSalarioError(Exception):
    def __init__(self,salario) -> None:
        super().__init__(f'{salario} No esta dentro del rango entre 1000 y 2000')

salario = int(input('Ingrese el salario'))

if salario >= 1000 and salario <= 2000:
    print('Su salario esta dentro del rango !')
else:
    raise RangoSalarioError(salario)