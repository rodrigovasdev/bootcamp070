SELECT  TO_NUMBER(TO_CHAR(VEN_FECHA, 'YYYY')) AS Periodo,
        CLI_NOMBRE AS NombreCliente,
        COUNT(*) AS CantidadCompras,
        SUM(TotalVenta) AS Total,
        CASE
            WHEN SUM(TotalVenta)<=150000 THEN 'Ocasional'
            WHEN SUM(TotalVenta)<=500000 THEN 'Gold'
                                         ELSE 'Premium' 
            END AS Clasificacion
FROM TB_VENTA
INNER JOIN (
            SELECT DET_VEN_NUMERO,
            SUM(DET_VALOR_UNITARIO * DET_CANTIDAD) AS TotalVenta
            FROM TB_DETALLE_VENTA
            GROUP BY DET_VEN_NUMERO
) DETALLE ON DET_VEN_NUMERO = VEN_NUMERO
INNER JOIN TB_CLIENTE ON CLI_RUT = VEN_CLI_RUT
WHERE TO_NUMBER(TO_CHAR(VEN_FECHA, 'YYYY')) = 2021
GROUP BY TO_NUMBER(TO_CHAR(VEN_FECHA, 'YYYY')), CLI_NOMBRE