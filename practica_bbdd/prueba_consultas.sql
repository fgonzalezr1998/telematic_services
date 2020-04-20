/*
-- 1.Listado de automoviles por clientes
SELECT Nombre, Apellido1, Apellido2, Marca, Modelo, Matricula
  FROM Clientes, Automoviles
  WHERE Clientes.DNI = Automoviles.DNI_Dueno;

-- 2.Horas trabajadas por empleado y mes
SELECT Nombre, Apellido1, Apellido2, Empleados.DNI, Suma_Horas, Mes
  FROM(
    SELECT DNI_Empleado AS'DNI', sum(Horas) AS'Suma_Horas', Mes
      FROM Facturas
        GROUP BY DNI, Mes
  ) AS'Subconsulta', Empleados

  WHERE Empleados.DNI = Subconsulta.DNI

-- 3.Media de horas que invierte cada empleado en cada trabajo distinto
SELECT Nombre, Apellido1, Apellido2, Empleados.DNI, Media_Horas, ID_Trabajo
  FROM(
      SELECT DNI_Empleado AS'DNI', avg(Horas) AS'Media_Horas', ID_Trabajo
        FROM Facturas
        GROUP BY DNI, ID_Trabajo
  ) AS'Subconsulta', Empleados

  WHERE Empleados.DNI = Subconsulta.DNI

*/
-- 4.Consultar Dinero gastado por clientes

SELECT (SELECT Precio_Ud * NV FROM Repuestos WHERE Nombre = "Ventanas"),
        (SELECT Precio_Ud * NP FROM Repuestos WHERE Nombre = "Puertas"),
        (SELECT Precio_Ud * NR FROM Repuestos WHERE Nombre = "Ruedas"),
        (SELECT Precio_Ud * NM FROM Repuestos WHERE Nombre = "Motores"),
        DNI_Cliente
  FROM(
      SELECT DNI_Cliente, sum(Num_Ventanas) AS'NV', sum(Num_Puertas) AS'NP', sum(Num_Ruedas) AS'NR', sum(Num_Motores) AS'NM'
        FROM Facturas
        GROUP BY DNI_Cliente
  )
/*
-- 5.Consultar las facturas pendientes
SELECT *
  FROM Facturas
  WHERE Cobrada = 0


-- 6.Consultar facturas pendientes por cliente

SELECT DNI_Cliente, Nombre, Apellido1, Apellido2, Cobrada
  FROM Facturas, Clientes
  --GROUP BY DNI_Cliente
  --HAVING DNI_Cliente = Clientes.DNI and Cobrada = 0
  WHERE DNI_Cliente = Clientes.DNI and Cobrada = 0
*/
