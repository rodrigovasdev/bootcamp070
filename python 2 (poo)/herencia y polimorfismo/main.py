from persona import Persona, Supervisor, Cliente, SupervisorZona

persona1 = Persona('Rodrigo', 'Vasquez','123456')
persona2 = Persona('José', 'Sanchez','456789')

supervisor1 = Supervisor('Juan', 'Perez','123456','Sur')
cliente1 = Cliente('José', 'Sanchez','456789',20)

superSupervisor = SupervisorZona('Rodrigo','Sanchez','109392820','Oriente',7,109,123)
superSupervisor.imprimir_supervisor_zona()

print(SupervisorZona.__mro__)
print(Supervisor.__mro__)
print(Persona.__mro__)


