-- Tabla Empresa
CREATE TABLE Empresa (
    Rut         VARCHAR(10) PRIMARY KEY NOT NULL,
    Nombre      VARCHAR(120) NOT NULL,
    Direccion   VARCHAR(120) NOT NULL,
    Telefono    VARCHAR(15) NOT NULL,  
    Correo      VARCHAR(80) NOT NULL,  
    Web         VARCHAR(50) NOT NULL      
);

-- Tabla Cliente
CREATE TABLE Cliente (
    Rut         VARCHAR(10) PRIMARY KEY NOT NULL,
    Nombre      VARCHAR(120) NOT NULL,
    Correo      VARCHAR(80) NOT NULL,  
    Direccion   VARCHAR(120) NOT NULL,
    Celular     VARCHAR(15) NOT NULL
);

-- Tabla Herramienta
CREATE TABLE Herramienta (
    IDHerramienta   NUMERIC(12) PRIMARY KEY NOT NULL,
    Nombre          VARCHAR(120) NOT NULL,
    PrecioDia       NUMERIC(12) NOT NULL 
);

-- Tabla Arriendo
CREATE TABLE Arriendo (
    Folio                       NUMERIC(12) PRIMARY KEY NOT NULL,
    Fecha                       DATE NOT NULL,
    Dias                        NUMERIC(5) NOT NULL,
    ValorDia                    NUMERIC(12) NOT NULL,  
    Garantia                    VARCHAR(30) NOT NULL,  
    Herramienta_IDHerramienta   NUMERIC(12) NOT NULL,  
    Cliente_RUT                 VARCHAR(10) NOT NULL,
    CONSTRAINT Arriendo_Herramienta_FK FOREIGN KEY (Herramienta_IDHerramienta) REFERENCES Herramienta(IDHerramienta),
    CONSTRAINT Arriendo_Cliente_FK FOREIGN KEY (Cliente_RUT) REFERENCES Cliente(Rut)  
);


