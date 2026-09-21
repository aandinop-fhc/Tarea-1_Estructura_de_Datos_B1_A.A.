#Ejercicio Propuesto
#IA
a = int(input("a: "))
b = int(input("b: "))

# Intercambio pythónico (una sola línea)
a, b = b, a

print(f"a = {a}, b = {b}")


#Hecho
    #Bosquejo
    #num1 = 5, num2 = 8

    #Intercambio: num1 pasa a valer lo que tenía num2, y num2 lo que tenía num1
    #num1 = 8, num2 = 5

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

num1, num2 = num2, num1

print(f"num1 = {num1}, num2 = {num2}")