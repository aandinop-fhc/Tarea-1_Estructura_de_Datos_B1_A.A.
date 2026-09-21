#Ejercicio Propuesto
#IA
n = int(input("¿Cuántos? "))
a, b = 0, 1                         # asignación múltiple

for _ in range(n):                  # _ porque no usamos el índice
    print(a, end=" ")
    a, b = b, a + b                 # avanzamos la serie

print()                             # salto de línea final

#Hecho
    #Bosquejo
    #n = 8

    #anterior = 0, actual = 1 (INICIALIZACIÓN)
    #serie = [0, 1]

    #siguiente = 0 + 1 = 1  → anterior=1, actual=1  → serie=[0,1,1]
    #siguiente = 1 + 1 = 2  → anterior=1, actual=2  → serie=[0,1,1,2]
    #siguiente = 1 + 2 = 3  → anterior=2, actual=3  → serie=[0,1,1,2,3]
    #... y así hasta completar 8 números

n = int(input("¿Cuántos? "))

serie = [0, 1]
anterior = 0
actual = 1

while len(serie) < n:
    siguiente = anterior + actual
    serie.append(siguiente)

    anterior = actual
    actual = siguiente

for numero in serie:
    print(numero, end=" ")

print()