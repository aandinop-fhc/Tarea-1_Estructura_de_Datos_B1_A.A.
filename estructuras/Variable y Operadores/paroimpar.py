#Taller 2
#IA
    #Bosquejo
    #num = 7

    #7 / 2 = 3, sobra 1 → impar
    #4 / 2 = 2, sobra 0 → par
    #0 / 2 = 0, sobra 0 → par (el cero es par)

num = int(input("Ingresa un número: "))

# Ternario: expresión que devuelve un valor u otro según la condición
resultado = "par" if num % 2 == 0 else "impar"

print(f"{num} es {resultado}")

#Ampliado
    #Bosquejo
    #num = 10
    #10 % 2 = 0 → par
    #10 % 3 = 1 → no divisible entre 3
    #10 % 5 = 0 → sí divisible entre 5

num = int(input("Ingresa un número: "))

# Ternario: expresión que devuelve un valor u otro según la condición
resultado = "par" if num % 2 == 0 else "impar"
if num % 3 == 0:
    print(f"{num} es divisible entre 3")
elif num % 5 == 0:
        print(f"{num} es divisible entre 5")
print(f"{num} es {resultado}")