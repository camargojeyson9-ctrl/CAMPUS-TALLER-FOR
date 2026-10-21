print("\n---RESULTADOS PRUEBA DE CICLISMO---")

n_ciclistas = int(input("Ingresa el numero de ciclistas: "))

mejor_tiempo = 999999.0 
ganador_id = ""

for veces in range(n_ciclistas):
    registro = int(input("\nIngresa el numero de registro del conductor: "))
    minutos = int(input("Ingresa los minutos: "))
    segundos = int(input("Ingresa los segundos: "))
    centesimas = int(input("Ingresa las centésimas: "))
    
    tiempo_segundos = 60 * minutos + segundos + centesimas / 100
    velocidad = 900 / tiempo_segundos

    print(f"{registro}: {velocidad:.2f} km/h", end=". ")
    
    if tiempo_segundos < mejor_tiempo:
        mejor_tiempo = tiempo_segundos
        ganador_id = registro

print(f"Ganador: {ganador_id}")