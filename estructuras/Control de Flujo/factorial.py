#Taller 3
#IA
    #Bosquejo
    #n = 5, fact = 1 (INICIALIZACIÓN)

    #i=1:  fact = 1 * 1 = 1
    #i=2:  fact = 1 * 2 = 2
    #i=3:  fact = 2 * 3 = 6
    #i=4:  fact = 6 * 4 = 24
    #i=5:  fact = 24 * 5 = 120   ← resultado

n = int(input("N: "))
fact = 1                    # INICIALIZACIÓN: 1 porque vamos a multiplicar

for i in range(1, n + 1):
    fact = fact * i         # o: fact *= i

print(f"{n}! = {fact}")

#Ampliado
    #Bosquejo
    #n = 5

    #factorial(5):
    #  5 * factorial(4)
    #  4 * factorial(3)
    #  3 * factorial(2)
    #  2 * factorial(1)
    #  caso base → retorna 1
    #  2 * 1 = 2
    #  3 * 2 = 6
    #  4 * 6 = 24
    #  5 * 24 = 120   ← resultado

def factorial(n):
    if n <= 1:              # CASO BASE: detiene la recursión
        return 1
    return n * factorial(n - 1)   # LLAMADA RECURSIVA

n = int(input("N: "))
print(f"{n}! = {factorial(n)}")