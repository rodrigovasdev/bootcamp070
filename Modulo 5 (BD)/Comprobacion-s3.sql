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
    Celular     VARCHAR(15) NOT NULL,  
    Alta        VARCHAR(1) NOT NULL      
);

-- Tabla Marca
CREATE TABLE Marca (
    IDMarca    NUMERIC(12) PRIMARY KEY NOT NULL,
    Nombre     VARCHAR(120)     
);

-- Tabla TipoVehiculo
CREATE TABLE TipoVehiculo (
    IDTipoVehiculo  NUMERIC(12) PRIMARY KEY NOT NULL,
    Nombre          VARCHAR(120)     
);

-- Tabla Vehiculo
CREATE TABLE Vehiculo (
    IDVehiculo                  NUMERIC(12) PRIMARY KEY NOT NULL,
    Patente                     VARCHAR(10) NOT NULL, 
    Marca                       VARCHAR(20) NOT NULL,   
    Modelo                      VARCHAR(20) NOT NULL, 
    Color                       VARCHAR(15) NOT NULL,
    Precio                      NUMERIC(12) NOT NULL,
    FrecuenciaMantencion        NUMERIC(5) NOT NULL,
    Marca_IDMarca               NUMERIC(12) NOT NULL,
    TipoVehiculo_IDTipoVehiculo NUMERIC(12) NOT NULL, 
    CONSTRAINT Vehiculo_Marca_FK FOREIGN KEY (Marca_IDMarca) REFERENCES Marca(IDMarca),
    CONSTRAINT Vehiculo_TipoVehiculo_FK FOREIGN KEY (TipoVehiculo_IDTipoVehiculo) REFERENCES TipoVehiculo(IDTipoVehiculo)
);

-- Tabla Venta
CREATE TABLE Venta (
    Folio       NUMERIC(12) PRIMARY KEY NOT NULL,
    Fecha       DATE NOT NULL,
    Monto       NUMERIC(12) NOT NULL,  
    Vehiculo_IDVehiculo  NUMERIC(12) NOT NULL,
    Cliente_RUT VARCHAR(10),
    CONSTRAINT Venta_Cliente_FK FOREIGN KEY (Cliente_RUT) REFERENCES Cliente(Rut),
    CONSTRAINT Venta_Vehiculo_FK FOREIGN KEY (Vehiculo_IDVehiculo) REFERENCES Vehiculo(IDVehiculo),
    UNIQUE (Vehiculo_IDVehiculo)    
);

-- Tabla Mantencion
CREATE TABLE Mantencion (
    IDMantencion NUMERIC(12) NOT NULL,
    Fecha        DATE NOT NULL,
    TrabajosRealizados VARCHAR(1000) NOT NULL,
    VentaFolio   NUMERIC(12) NOT NULL,
    CONSTRAINT Mantencion_PK PRIMARY KEY (IDMantencion),
    CONSTRAINT Mantencion_Venta_FK FOREIGN KEY (VentaFolio) REFERENCES Venta(Folio)
);