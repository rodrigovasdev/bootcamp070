--1 req
SELECT * 
FROM cliente
WHERE NOT EXISTS (SELECT cliente_rut FROM arriendo)

--2 req
SELECT folio, fecha, dias,valordia,nombre,cliente_rut
FROM arriendo
JOIN (
    SELECT rut, nombre
    FROM cliente
) datosCliente ON arriendo.cliente_rut = datosCliente.rut;

--3 req
SELECT cliente.nombre, COUNT (arriendo.cliente_rut) AS "Ctdad arriendos",
			CASE
            WHEN COUNT (arriendo.cliente_rut)<2    THEN 'Bajo'
			WHEN COUNT (arriendo.cliente_rut)<3 	THEN 'Medio'
													ELSE 'Alto' 
            END AS Clasificacion
FROM arriendo
JOIN cliente ON arriendo.cliente_rut = cliente.rut
WHERE cliente.rut = arriendo.cliente_rut
GROUP BY cliente.nombre

--4 req
SELECT cliente.nombre AS Nombre,
	   herramienta.nombre AS NombreHerramienta
FROM cliente
JOIN arriendo
ON cliente.rut = arriendo.cliente_rut
JOIN herramienta
ON arriendo.herramienta_idherramienta = herramienta.Idherramienta
WHERE herramienta.Idherramienta IN  (SELECT herramienta_Idherramienta AS id
									 FROM arriendo
									 GROUP BY id
									 ORDER BY COUNT(herramienta_Idherramienta) DESC
									 );
