# Organizo las entradas del ejercicio.

print("---PROGRESION ARITMETICA")

termA = int(input("\nIngrese el Termino A: "))
termD = int(input("Ingrese el Termino D: "))
termN = int(input("Ingrese el termino N: "))

# Coloco los limites

if -100 <= termA <= 100 and -100 <= termD <= 100 and 0 <= termN <= 1000:
    suma = 0
    termino_actual = termA

# Creo el condicional For
 
    for operacion in range(termN):
        suma = suma + termino_actual
        termino_actual = termino_actual + termD

    print("Suma:",suma)

else:
    print("Valores invalidos")
