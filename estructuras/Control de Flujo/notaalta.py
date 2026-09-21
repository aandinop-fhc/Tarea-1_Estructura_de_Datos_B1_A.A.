#Taller 3
#IA
    #Bosquejo
    #nota máxima = -infinito (o = primera nota)

    #leo 6  → 6 > -inf → máx = 6
    #leo 9  → 9 > 6   → máx = 9
    #leo 4  → 4 > 9   → NO cambia
    #leo 8  → 8 > 9   → NO cambia
    #leo 10 → 10 > 9  → máx = 10

    #resultado: 10

n = int(input("¿Cuántas notas? "))
maxima = float("-inf")             

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota > maxima:               
        maxima = nota               

print(f"Máxima: {maxima}")

#Ampliado
    #Bosquejo
    #n = 3, minima = inf (INICIALIZACIÓN: cualquier nota será menor que infinito)

    #nota 1 = 8   → 8 < inf → sí   → minima = 8
    #nota 2 = 5   → 5 < 8   → sí   → minima = 5
    #nota 3 = 9   → 9 < 5   → no   → minima sigue en 5

    #resultado: minima = 5

n = int(input("¿Cuántas notas? "))
minima = float("inf")             

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota < minima:               
        minima = nota               

print(f"Minima: {minima}")