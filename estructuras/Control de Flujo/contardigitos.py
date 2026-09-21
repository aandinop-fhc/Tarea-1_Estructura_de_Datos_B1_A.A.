#Ejercicio Produesto
#IA
num = int(input("Número: "))
n = abs(num)                # trabajar con el positivo
digitos = 0

if n == 0:
    digitos = 1             # caso especial: el 0 tiene 1 dígito
else:
    while n > 0:
        digitos += 1
        n = n // 10         # quitamos el último dígito

print(f"{digitos} dígitos")

#Hecho 
    #Bosquejo
    #numero = 12345

    #12345 // 10 = 1234   → llevamos 1
    #1234  // 10 = 123    → llevamos 2
    #123   // 10 = 12     → llevamos 3
    #12    // 10 = 1      → llevamos 4
    #1     // 10 = 0      → llevamos 5 → se detiene

numero = int(input("Número: "))
valor = abs(numero)              # trabajar con el positivo

contador = 1 if valor == 0 else 0

while valor > 0:
    valor = valor // 10
    contador = contador + 1

print(f"{contador} dígitos")