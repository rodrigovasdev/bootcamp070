--1 req
SELECT *
FROM cliente
WHERE NOT EXISTS (SELECT Cliente_rut FROM venta)

--2 req
SELECT folio, fecha, monto,rut,nombre
FROM venta
JOIN (
    SELECT rut, nombre
    FROM cliente
) datosCliente ON venta.cliente_rut = datosCliente.rut;

--3 req
SELECT cliente_rut,monto,
			CASE
            WHEN SUM(Monto)<=1000000 	  THEN 'Estandar'
			WHEN SUM(Monto)<=3000000 	  THEN 'Gold'
                                         ELSE 'Premium' 
            END AS Clasificacion
FROM venta
GROUP BY cliente_rut,monto

--4 req
SELECT * 
FROM venta
WHERE vehiculo_idvehiculo IN (SELECT idvehiculo
							   FROM vehiculo
							   WHERE marca IN 
								   (SELECT vehiculo.marca AS marca
									FROM vehiculo
									JOIN venta ON vehiculo.idvehiculo = venta.vehiculo_idvehiculo
									GROUP BY marca
									ORDER BY COUNT(vehiculo.marca) DESC
									LIMIT 1))
