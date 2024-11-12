--1 req
SELECT arriendo.folio,arriendo.fecha,arriendo.dias,arriendo.valordia, cliente.nombre as nombreCliente, cliente.rut as rutCliente
FROM arriendo
JOIN cliente ON arriendo.cliente_rut = cliente.rut


--2 req
SELECT * 
FROM cliente
RIGHT JOIN arriendo ON cliente.rut = arriendo.cliente_rut
WHERE arriendo.cliente_rut IS NULL

--3 req
SELECT 'Empresa' as Entidad, rut, nombre FROM empresa
UNION
SELECT 'Cliente' as Entidad, rut, nombre FROM cliente

--4 req
SELECT to_char("fecha",'MM') AS mes, COUNT(folio)
FROM arriendo
GROUP BY to_char("fecha",'MM')