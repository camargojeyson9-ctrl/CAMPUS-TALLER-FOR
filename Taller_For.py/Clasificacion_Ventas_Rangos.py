print("---CLASIFICACION DE VENTAS TRES RANGOS---")

nventas = int(input("Ingresa el numero de ventas: "))
grupo1=0
grupo2=0
grupo3=0

for veces in range(nventas):
    importe=int(input("Ingrese el importe de la venta: "))
    if importe <= 200:
        grupo1 += 1
    
    elif importe <400:
        grupo2 += 1
    
    elif importe >=400:
        grupo3 += 1

    else:
        print("Valor invalido, vuelve a intentarlo!")

print("Grupos 1, 2 y 3:",grupo1,grupo2,grupo3)

