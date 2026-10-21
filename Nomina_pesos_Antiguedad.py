print("\n--- NOMINA CON PESOS DE ANTIGUEDAD ---")

N = int(input("\nIngrese la cantidad de empleados (1 a 40): "))

# Variables acumuladoras y de control para mayor/menor sueldo
total_nomina = 0.0
mayor_sueldo = 0.0
menor_sueldo = 999999.0
id_mayor = -1
id_menor = -1
suma_antiguedad = 0.0

for i in range(N):
    id_empleado = int(input("\nIngrese el identificador: "))
    edad = int(input("Ingrese la edad: "))
    antiguedad = int(input("Ingrese los años de antigüedad (1 a 50): "))
    
    for j in range(1, antiguedad + 1):
        suma_antiguedad = suma_antiguedad + antiguedad
        
    sueldo = (100 + edad + suma_antiguedad) / antiguedad
    
    print(f"Sueldo del empleado {id_empleado}: {sueldo}")
    
    total_nomina = total_nomina + sueldo
    
    if sueldo > mayor_sueldo:
        mayor_sueldo = sueldo
        id_mayor = id_empleado
        
    if sueldo < menor_sueldo:
        menor_sueldo = sueldo
        id_menor = id_empleado


print(f"\nTotal de la nómina: {total_nomina}")
print(f"Identificador con mayor sueldo: {id_mayor} (Sueldo: {mayor_sueldo})")
print(f"Identificador con menor sueldo: {id_menor} (Sueldo: {menor_sueldo})")
