#Ejercicio Propuesto
#AI
datos = ["a", "b", "a", "c", "b", "d"]
vistos = set()
resultado = []
for x in datos:
    if x not in vistos:
        vistos.add(x)
        resultado.append(x)
print(resultado)  # ['a', 'b', 'c', 'd']


#Hecho
    #Bosquejo
    #elementos = ["a", "b", "a", "c", "b", "d"]

    #"a" → nuevo → se agrega
    #"b" → nuevo → se agrega
    #"a" → repetido → se ignora
    #"c" → nuevo → se agrega
    #"b" → repetido → se ignora
    #"d" → nuevo → se agrega

    #resultado: ["a", "b", "c", "d"]

elementos = ["b","a", "b", "a", "c", "b", "d","c"]

ya_agregados = set()
sin_duplicados = []

for elemento in elementos:
    esta_repetido = elemento in ya_agregados

    if not esta_repetido:
        sin_duplicados.append(elemento)
        ya_agregados.add(elemento)

print(sin_duplicados)