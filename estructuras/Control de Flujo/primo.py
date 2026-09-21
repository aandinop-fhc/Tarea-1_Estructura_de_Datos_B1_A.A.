#
#
    #Bosquejo
    #n = 17, es_primo = True (bandera)

    #Pruebo divisores del 2 al √17 ≈ 4:
    #  17 % 2 = 1 (no divide)
    #  17 % 3 = 2 (no divide)
    #  17 % 4 = 1 (no divide)

    #Ninguno dividió → 17 es primo ✓

n = int(input("Número: "))
es_primo = True                     # BANDERA: asumimos que sí

if n < 2:
    es_primo = False                # 0 y 1 no son primos
else:
    # Probar divisores del 2 hasta √n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:              # si i divide exacto a n...
            es_primo = False        # ...no es primo
            break                   # optimización: no seguir probando

if es_primo:
    print(f"{n} es primo")
else:
    print(f"{n} NO es primo")

#Ampliado
    #Bosquejo

    #num = 17, es_primo = True (bandera)
    #  17 % 2 = 1 (no divide)
    #  17 % 3 = 2 (no divide)
    #  17 % 4 = 1 (no divide)
    #Ninguno dividió → 17 es primo ✓ → se agrega a la lista

    #num = 18, es_primo = True (bandera)
    #Pruebo divisores del 2 al √18 ≈ 4:
    #  18 % 2 = 0 (sí divide) → es_primo = False
    #No es primo ✗ → no se agrega

primos = []

for n in range(2, 101):
    es_primo = True                     

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:                  
            es_primo = False            
            break                       

    if es_primo:
        primos.append(n)

print(primos)