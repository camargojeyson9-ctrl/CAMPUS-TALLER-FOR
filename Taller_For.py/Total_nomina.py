print("---TOTAL NOMINA---")

num_empleados = int(input("Ingrese el numero de empleados: "))

nomina = 0

for veces in range(1, num_empleados+1):
    sueldo = int(input("Ingresa el sueldo del empleado: "))

    nomina = sueldo + nomina

print ("Nomina: ", nomina)