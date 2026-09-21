#Ejercicio Propuesto
#IA
import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina (1-100): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Es mayor")
    else:
        print("Es menor")


#Hecho
    #Bosquejo
    #numero_secreto = 42, contador_intentos = 0

    #intento 1: 50 → 42 < 50 → "Es menor" → contador_intentos = 1
    #intento 2: 30 → 42 > 30 → "Es mayor" → contador_intentos = 2
    #...
    #intento 6: 42 → coincide → adivinado = True → contador_intentos = 6

import random

numero_secreto = random.randint(1, 100)
contador_intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina (1-100): "))
    contador_intentos = contador_intentos + 1

    if intento == numero_secreto:
        adivinado = True
    elif intento > numero_secreto:
        print("Es menor")
    else:
        print("Es mayor")

print(f"¡Correcto en {contador_intentos} intentos!")