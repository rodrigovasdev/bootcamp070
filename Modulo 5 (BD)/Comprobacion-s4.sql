-- Tabla Departamentos
CREATE TABLE Departamentos (
    ID         INTEGER PRIMARY KEY,
    Nombre     VARCHAR(100),
    Ubicacion  VARCHAR(100)     
);

-- Tabla Empleados
CREATE TABLE Empleados (
    ID         INTEGER PRIMARY KEY,
    Nombre     VARCHAR(100),
    Puesto     VARCHAR(100),   
    Salario    NUMERIC(10,2),
    Fecha_contratacion DATE,
    Departamento_id INTEGER,
    CONSTRAINT Empleados_Departamento_FK FOREIGN KEY (Departamento_id) REFERENCES Departamentos(ID)
);


-- Punto 4)
ALTER TABLE Empleados ADD (email VARCHAR(100));

-- Punto 5)
ALTER TABLE Empleados RENAME TO Trabajadores;

-- Punto 6)
DROP TABLE Departamentos CASCADE;