#Ejercicio Propuesto
#IA
n = int(input("¿Cuántos números? "))
suma_pares = 0
suma_impares = 0

for i in range(n):
    x = int(input(f"Número {i+1}: "))
    if x % 2 == 0:
        suma_pares += x
    else:
        suma_impares += x

print(f"Suma pares: {suma_pares}")
print(f"Suma impares: {suma_impares}")

#Hecho
    #Bosquejo
    #cantidad = 5, numeros = 4 7 2 9 6

    #4 % 2 = 0 → par   → total_pares = 4
    #7 % 2 = 1 → impar → total_impares = 7
    #2 % 2 = 0 → par   → total_pares = 4 + 2 = 6
    #9 % 2 = 1 → impar → total_impares = 7 + 9 = 16
    #6 % 2 = 0 → par   → total_pares = 6 + 6 = 12

cantidad = int(input("¿Cuántos números? "))

total_pares = 0
total_impares = 0

for posicion in range(1, cantidad + 1):
    valor = int(input(f"Número {posicion}: "))

    es_par = valor % 2 == 0

    if es_par:
        total_pares = total_pares + valor
    else:
        total_impares = total_impares + valor

print(f"Suma pares: {total_pares}")
print(f"Suma impares: {total_impares}")