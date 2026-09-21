#Taller 4
#IA
    #Bosquejo
    #suma_digitos(4783):
    #  suma = 0
    #  4783 % 10 = 3   → suma = 3,  n = 478
    #   478 % 10 = 8   → suma = 11, n = 47
    #    47 % 10 = 7   → suma = 18, n = 4
    #     4 % 10 = 4   → suma = 22, n = 0
    #  fin → return 22

def suma_digitos(n):
    n = abs(n)                     # por si es negativo
    suma = 0
    while n > 0:
        suma += n % 10             # último dígito
        n = n // 10                # quita el último dígito
    return suma

# Uso
num = int(input("Número: "))
print(f"Suma: {suma_digitos(num)}")

# También sirve para varios
for x in [123, 4783, 999]:
    print(f"{x} → {suma_digitos(x)}")


#Ampliada
    #Bosquejo
    #es_narcisista(153)

    #Primero cuento cuántos dígitos tiene: 153 tiene 3 cifras

    #Reviso dígito por dígito, igual que en suma_digitos, pero elevando cada uno a 3:
    #153 % 10 = 3 → 3**3 = 27  → suma = 27      | 153 // 10 = 15
    #15  % 10 = 5 → 5**3 = 125 → suma = 152     | 15  // 10 = 1
    #1   % 10 = 1 → 1**3 = 1   → suma = 153     | 1   // 10 = 0 → termina

    #suma (153) == número original (153) → True → SÍ es narcisista

def es_narcisista(n):
    numero_original = n
    n = abs(n)

    cifras = len(str(n))          # cuántos dígitos tiene

    suma = 0
    while n > 0:
        suma += (n % 10) ** cifras
        n = n // 10

    return suma == numero_original

# Uso
num2 = int(input("¿Número a revisar (narcisista)?: "))
print(f"{num2} → {'narcisista' if es_narcisista(num2) else 'no narcisista'}")