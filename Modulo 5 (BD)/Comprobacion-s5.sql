-- Tabla Editorial
CREATE TABLE Editorial (
    Codigo        INTEGER PRIMARY KEY,
    Nombre     VARCHAR(100)
);

-- Tabla Libro
CREATE TABLE Libro (
    Codigo       INTEGER PRIMARY KEY,
    Nombre     VARCHAR(100),
    Cod_editorial     INTEGER,
    CONSTRAINT Libro_Editorial_FK FOREIGN KEY (Cod_editorial) REFERENCES Editorial(Codigo)
);

-- Insert Tabla Editorial
INSERT INTO public.editorial(
	        codigo, nombre)
	VALUES  (1, 'Anaya'),
            (2, 'Andina'),
            (3, 'S.M.');

-- Insert Tabla Libro
INSERT INTO public.libro(
	        codigo, nombre, cod_editorial)
	VALUES  (1, 'Don Quijote de La Mancha I', 1),
            (2, 'El principito', 2),
            (3, 'El príncipe', 3),
            (4, 'Diplomacia', 3),
            (5, 'Don Quijote de La Mancha II', 1);

-- Punto 4)
ALTER TABLE Libro ADD autor VARCHAR(100);
ALTER TABLE Libro ADD precio NUMERIC;

-- Punto 5)
UPDATE public.libro
	SET autor='Miguel de Cervantes', precio=150
	WHERE codigo = 1;

UPDATE public.libro
	SET autor='Antoine SaintExupery', precio=120
	WHERE codigo = 2;

UPDATE public.libro
	SET autor='Maquiavelo', precio=180
	WHERE codigo = 3;

UPDATE public.libro
	SET autor='Henry Kissinger', precio=170
	WHERE codigo = 4;

UPDATE public.libro
	SET autor='Miguel de Cervantes', precio=140
	WHERE codigo = 5;

-- Insert Tabla Libro Punto 6)
INSERT INTO public.libro(
	        codigo, nombre, cod_editorial, autor, precio)
	VALUES  (6, 'El castillo encantado', 1,'Rodrigo Vasquez',120),
            (7, 'El tunel sin fin', 2,'Juan Perez',90)

-- Punto 7)
BEGIN;
DELETE FROM public.libro
	WHERE cod_editorial = 2;
ROLLBACK;


-- Punto 8)
BEGIN;
UPDATE public.editorial
	SET nombre='Mountain'
	WHERE codigo = 3;
SAVEPOINT puntodeguardado;

UPDATE public.editorial
	SET nombre='Iberlibro'
	WHERE codigo = 2;
ROLLBACK TO SAVEPOINT puntodeguardado;
COMMIT;

