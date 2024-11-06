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



