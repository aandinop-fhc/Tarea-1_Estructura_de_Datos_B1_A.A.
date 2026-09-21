#Ejercicio Propuesto
#IA
texto = "El perro y el gato y el perro"
conteo = {}
for palabra in texto.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)

mas = max(conteo, key=conteo.get)
print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")


#Hecho
    #Bosquejo (corto)
    #frase = "El sol brilla y el cielo brilla y el sol"

    #"el"     → nuevo    → conteo["el"] = 1
    #"sol"    → nuevo    → conteo["sol"] = 1
    #"brilla" → nuevo    → conteo["brilla"] = 1
    #"y"      → nuevo    → conteo["y"] = 1
    #"el"     → repetido → conteo["el"] = 2
    #"cielo"  → nuevo    → conteo["cielo"] = 1
    #"brilla" → repetido → conteo["brilla"] = 2
    #"y"      → repetido → conteo["y"] = 2
    #"el"     → repetido → conteo["el"] = 3
    #"sol"    → repetido → conteo["sol"] = 2

    #resultado: {'el': 3, 'sol': 2, 'brilla': 2, 'y': 2, 'cielo': 1}
    #más repetida: 'el' (3 veces)

frase = "El sol brilla y el cielo brilla y el sol"
conteo = {}

for palabra in frase.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)

palabra_top = max(conteo, key=conteo.get)
print(f"Más repetida: '{palabra_top}' ({conteo[palabra_top]} veces)")