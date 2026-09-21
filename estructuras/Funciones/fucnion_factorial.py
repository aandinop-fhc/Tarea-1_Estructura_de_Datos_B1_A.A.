#Ejercicio Propuesto
#IA
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def combinatoria(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Uso
print(factorial(5))            # 120
print(combinatoria(5, 2))      # 10 = 5!/(2!·3!) = 120/12

#Bosquejo
#factorial(5)
#5 * factorial(4)
#4 * factorial(3)
#3 * factorial(2)
#2 * factorial(1)
#caso base → retorna 1
#2 * 1 = 2
#3 * 2 = 6
#4 * 6 = 24
#5 * 24 = 120

#combinatoria(5, 2) = factorial(5) / (factorial(2) * factorial(5-2))
#                    = 120 / (2 * 6) = 120 / 12 = 10

def factorial(numero):
    if numero <= 1:
        return 1
    return numero * factorial(numero - 1)

def combinatoria(elementos, grupo):
    numerador = factorial(elementos)
    denominador = factorial(grupo) * factorial(elementos - grupo)
    return numerador // denominador

# Uso
print(factorial(5))            # 120
print(combinatoria(5, 2))      # 10
