#Taller 4
#IA
    #Bosquejo
    #es_primo(7) → devuelve True
    #es_primo(10) → devuelve False
    #es_primo(1) → devuelve False

    #Uso: if es_primo(numero): ...

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False           # sale inmediatamente
    return True                    # llegó al final sin encontrar divisor

# --- Uso 1: verificar uno ---
num = int(input("Número: "))
if es_primo(num):
    print(f"{num} es primo")
else:
    print(f"{num} NO es primo")

# --- Uso 2: listar primos entre 2 y 30 ---
print("Primos entre 2 y 30:")
for k in range(2, 31):
    if es_primo(k):
        print(k, end=" ")


#Ampliado
    #Bosquejo

    #--- es_primo(7) ---
    #7 no es menor que 2
    #raíz de 7 ≈ 2.6 → reviso solo i=2
    #7 % 2 = 1 (no divide) → no encontré divisor
    #retorna True → 7 es primo

    #--- es_primo(10) ---
    #10 no es menor que 2
    #raíz de 10 ≈ 3.1 → reviso i=2, i=3
    #10 % 2 = 0 (sí divide) → retorna False de inmediato
    #10 NO es primo

    #--- contar_primos(2, 10) ---
    #recorre n = 2..10, preguntando es_primo(n) para cada uno

    #n=2 → primo → contador = 1
    #n=3 → primo → contador = 2
    #n=4 → no primo
    #n=5 → primo → contador = 3
    #n=6 → no primo
    #n=7 → primo → contador = 4
    #n=8 → no primo
    #n=9 → no primo
    #n=10 → no primo

    #resultado: contador = 4


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False           
    return True                    
def contar_primos(a, b):
    contador = 0
    for n in range(a, b + 1):
        if es_primo(n):
            contador += 1
    return contador

num = int(input("Número: "))
if es_primo(num):
    print(f"{num} es primo")
else:
    print(f"{num} NO es primo")


print("Primos entre 2 y 30:")
for k in range(2, 31):
    if es_primo(k):
        print(k, end=" ")

print()
a = int(input("Desde: "))
b = int(input("Hasta: "))
print(f"Cantidad de primos entre {a} y {b}: {contar_primos(a, b)}")