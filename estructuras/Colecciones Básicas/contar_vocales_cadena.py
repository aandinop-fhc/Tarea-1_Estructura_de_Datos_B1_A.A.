#Ejercicio Propuesto
#AI
frase = input("Frase: ").lower()
vocales = {"a", "e", "i", "o", "u"}
total = 0
for ch in frase:
    if ch in vocales:
        total += 1
print(f"{total} vocales")


#Hecho
    #Bosquejo
    #texto = "Hola Mundo" → en minúsculas: "hola mundo"
    #vocales_validas = {"a", "e", "i", "o", "u"}

    #h → ¿está en vocales_validas? no
    #o → ¿está en vocales_validas? sí → contador = 1
    #l → no
    #a → sí → contador = 2
    #(espacio) → no
    #m → no
    #u → sí → contador = 3
    #n → no
    #d → no
    #o → sí → contador = 4

vocales_validas = {"a", "e", "i", "o", "u"}

texto = input("Frase: ").lower()
contador = 0

for letra in texto:
    es_vocal = letra in vocales_validas
    if es_vocal:
        contador += 1

print(f"{contador} vocales")