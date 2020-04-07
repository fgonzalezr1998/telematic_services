
-- 1. Listado de automoviles por clientes
SELECT Nombre, Apellido1, Apellido2, Marca, Modelo, Matricula
  FROM Clientes, Automoviles
  WHERE Clientes.DNI = Automoviles.DNI_Dueno;

-- 2. Horas trabajadas por empleado y mes
