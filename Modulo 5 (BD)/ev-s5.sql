-- Tabla pelicula
CREATE TABLE Pelicula (
    id          INTEGER PRIMARY KEY,
    titulo      VARCHAR(100),
    estreno     INTEGER,
    director     VARCHAR(100)
);

-- Tabla reparto
CREATE TABLE Reparto (
    id_pelicula 	INTEGER,
    actor      		VARCHAR(100),
	CONSTRAINT pelicula_pk PRIMARY KEY(id_pelicula,actor),
    CONSTRAINT reparto_pelicula_FK FOREIGN KEY (id_pelicula) REFERENCES Pelicula(id)
);

-- Punto 7
SELECT Pelicula.titulo, pelicula.estreno, pelicula.director,Reparto.actor
FROM Pelicula
JOIN Reparto ON Pelicula.id = Reparto.id_pelicula
WHERE Pelicula.id = 2

-- Punto 8
SELECT 
director,
COUNT(director) AS "en cuantas peliculas aparece"
FROM pelicula
GROUP BY
director
ORDER BY "en cuantas peliculas aparece" DESC
LIMIT 10;

-- Punto 9
SELECT 
COUNT(DISTINCT actor) AS "Actores distintos"
FROM reparto;

-- Punto 10
SELECT titulo
FROM pelicula
WHERE estreno >= 1990 AND estreno <= 1999
ORDER BY titulo ASC;

-- Punto 11
SELECT reparto.actor, pelicula.titulo, pelicula.estreno
FROM pelicula
JOIN reparto ON pelicula.id=reparto.id_pelicula
ORDER BY pelicula.estreno DESC
LIMIT 4;

-- Punto 12
BEGIN;
	INSERT INTO pelicula (id, titulo, estreno, director)
	VALUES (108, 'Pelicula que no se vera', 2019, 'Anthony Russo');
ROLLBACK;

BEGIN;
	INSERT INTO pelicula (id, titulo, estreno, director)
	VALUES (109, 'Pelicula que SI se vera', 2024, 'Anthony Russo');
COMMIT;

-- Punto 13
BEGIN;
UPDATE public.pelicula
	SET director= CASE director
	WHEN 'Steven Spielberg' THEN 'H Simpson'
	WHEN 'Ridley Scott' THEN 'Spiderman'
	WHEN 'William Wyler' THEN 'Superman'
	WHEN 'Hayao Miyazaki' THEN 'Batman'
	WHEN 'Brad Bird' THEN 'Linterna Verde'
	ELSE director
	END;
ROLLBACK;

-- Punto 14
BEGIN;
SAVEPOINT sp;
INSERT INTO public.reparto(
	id_pelicula, actor)
	VALUES (72, 'Rodrigo V'),(72, 'Don Quijote'),(72, 'Sancho Panza');
COMMIT;


-- 16.	Inserte 2 actores para cada película estrenada el 2001.

-- Ids de peliculas estrenadas el 2001:
-- 55
-- 78
-- 94
-- 99
-- 13
-- 16
INSERT INTO reparto VALUES('55','actor 1'),('55','actor 2'),
   						  ('78','actor 3'),('78','actor 4'),
   						  ('94','actor 5'),('94','actor 6'),
   						  ('99','actor 7'),('99','actor 8'),
   						  ('13','actor 9'),('13','actor 10'),
   						  ('16','actor 11'),('16','actor 12');
