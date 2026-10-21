"""
Entrada
numA : Primer numero del rango.
numB : Segundo numero del rango.

Proceso
Realizo un condicional For en el cual mediante dos valores buscaremos hallar un rango mediante Range.

Salida
Mostrarme el rango de acuerdo a las dos entradas.
"""

# Pido los dos numeros (Inicio y Fin), para calcular el rango.

print("\n---SECUENCIA ENTRE DOS LIMITES")

numA = int(input("\nIngrese el numero que da (Inicio) del rango: "))
numB = int(input("Ingrese el numero que (Finaliza) del rango: "))

print("\nA continuacion la secuencia entre dos limites")
print(list(range(numA, numB+1)))