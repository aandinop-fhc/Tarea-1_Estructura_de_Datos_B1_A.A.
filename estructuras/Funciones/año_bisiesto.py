#Ejercicio Propuesto
#IA
def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    if anio % 4 == 0:
        return True
    return False

# O en una línea:
def es_bisiesto_corta(anio):
    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)

# Pruebas
for y in [2024, 2023, 2000, 1900]:
    print(f"{y}: {es_bisiesto(y)}")


#Hecho
    #Bosquejo
    #anio = 2024

    #¿divisible entre 4?   → 2024 % 4 = 0   → sí
    #¿NO divisible entre 100? → 2024 % 100 = 24 → sí (no es divisible)
    #Como ambas son verdaderas → bisiesto = True

    #Caso especial: anio = 2000
    #¿divisible entre 400? → 2000 % 400 = 0 → sí → bisiesto = True (sin importar el 100)

def es_bisiesto(anio):
    divisible_4 = anio % 4 == 0
    no_divisible_100 = anio % 100 != 0
    divisible_400 = anio % 400 == 0

    bisiesto = (divisible_4 and no_divisible_100) or divisible_400
    return bisiesto

# Pruebas
for a in [2024, 2023, 2000, 1900]:
    print(f"{a}: {es_bisiesto(a)}")