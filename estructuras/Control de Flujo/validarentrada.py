#Ejercicio Propuesto
#IA
while True:
    edad = int(input("Edad (0-120): "))
    if 0 <= edad <= 120:
        break                       # sale del while
    print("Inválida, intenta de nuevo")

print(f"Edad válida: {edad}")

#Hecho
    #Bosquejo
    #Primer intento: edad = -5
    #  -5 no está entre 0 y 120 → entrada_valida = False → vuelve a pedir

    #Segundo intento: edad = 150
    #  150 no está entre 0 y 120 → entrada_valida = False → vuelve a pedir

    #Tercer intento: edad = 25
    #  25 sí está entre 0 y 120 → entrada_valida = True → sale del bucle

entrada_valida = False

while not entrada_valida:
    edad = int(input("Edad (0-120): "))

    if edad < 0 or edad > 120:
        print("Inválida, intenta de nuevo")
    else:
        entrada_valida = True

print(f"Edad válida: {edad}")