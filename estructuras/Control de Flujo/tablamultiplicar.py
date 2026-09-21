#Ejercicio Propuesto
#IA

n = int(input("Tabla de: "))

for i in range(1, 13):
    print(f"{n} × {i} = {n * i}")

#Hecho
    #Bosquejo
    #numero = 7

    #multiplicador = 1 → 7 × 1 = 7
    #multiplicador = 2 → 7 × 2 = 14
    #...
    #multiplicador = 12 → 7 × 12 = 84

numero = int(input("Tabla de: "))

multiplicador = 1
while multiplicador <= 12:
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    multiplicador += 1
