from persona import Persona, Supervisor, Cliente

persona1 = Persona('Rodrigo', 'Vasquez','123456')
persona2 = Persona('José', 'Sanchez','456789')

supervisor1 = Supervisor('Juan', 'Perez','123456','Sur')
cliente1 = Cliente('José', 'Sanchez','456789',20)

print(persona1.__dict__)

