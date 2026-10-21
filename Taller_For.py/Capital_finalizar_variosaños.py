print("\n---CAPITAL FINALIZAR VARIOS AÑOS---")

capitalc = int(input("\nIngrese el capital de inicio: "))
tasa_anual = int(input("Ingrese la tasa anual porcentual: "))
años = int(input("Ingrese el Numero M: "))

saldo = capitalc

for capital in range(años):
    saldo = saldo*(1+tasa_anual/100)

print("Saldo:", saldo)