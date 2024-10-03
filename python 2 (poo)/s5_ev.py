class Persona:
    def __init__(self,nombre,apellido,anno) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno

class Departamento:
    def __init__(self,nombre_dpto, nombre_corto_dpto) -> None:
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto

class Trabajador(Persona,Departamento):
    def __init__(self, nombre, apellido, anno,nombre_dpto,nombre_corto_dpto, salario) -> None:
        Persona.__init__(self,nombre, apellido, anno)
        Departamento.__init__(self,nombre_dpto,nombre_corto_dpto)
        self.salario = salario

trabajadorcito = Trabajador('Juan','Perez',2005,'Ing de software','IS',20000)
print(trabajadorcito.__dict__)
print(isinstance(trabajadorcito,Persona))
print(isinstance(trabajadorcito,Departamento))
print(isinstance(trabajadorcito,Trabajador))
        