# Ejercicio Propuesto
#IA
num = int(input("Número de 3 cifras: "))

centenas = num // 100
decenas = (num // 10) % 10
unidades = num % 10

suma = centenas + decenas + unidades
print(f"Suma: {suma}")

#Hecho
    #Bosquejo
    #numero = 435

    #Paso 1: separo la centena del resto
    #centena = 435 // 100 = 4
    #resto   = 435 % 100  = 35

    #Paso 2: de ese resto, separo decena y unidad
    #decena  = 35 // 10 = 3
    #unidad  = 35 % 10  = 5

    #suma = 4 + 3 + 5 = 12

numero = int(input("Número de 3 cifras: "))

centena = numero // 100
resto = numero % 100

decena = resto // 10
unidad = resto % 10

total = centena + decena + unidad

print(f"Suma: {total}")