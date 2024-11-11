-- Req 1
SELECT * FROM Vehiculo
LEFT JOIN Venta ON vehiculo.idvehiculo = Venta.Vehiculo_IDVehiculo
WHERE Venta.Vehiculo_IDVehiculo IS NULL

-- Req 2
SELECT  venta.folio AS folio,
		venta.fecha AS FechaVenta, 
		venta.monto AS MontoVenta, 
		cliente.nombre AS NombreCliente, 
		cliente.rut AS RutCliente, 
		vehiculo.patente AS Patente, 
		vehiculo.marca AS NombreMarca,
		vehiculo.modelo AS Modelo
FROM Venta
JOIN Cliente
ON Venta.cliente_RUT = cliente.RUT
JOIN Vehiculo
ON Venta.vehiculo_IDVehiculo = Vehiculo.IDVehiculo
WHERE to_char("fecha",'YYYY-MM') = '2020-01'

-- Req 3
SELECT venta.fecha, vehiculo.marca, SUM(venta.monto) AS suma_ventas
FROM venta
JOIN vehiculo ON venta.Vehiculo_IDVehiculo = vehiculo.IDVehiculo
WHERE to_char("fecha",'YYYY-MM') = '2020-01'
GROUP BY venta.fecha, vehiculo.marca

-- Req 4
SELECT nombre, rut FROM empresa
UNION
SELECT nombre, rut FROM cliente