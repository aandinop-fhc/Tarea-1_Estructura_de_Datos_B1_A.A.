#Taller 3
#IA
    #Bosquejo
    #n = 4, aprobados = 0 (INICIALIZACIÓN)

    #ota=8 → 8 >= 7 → aprobados = 1
    #nota=5 → 5 >= 7 → NO cambia
    #nota=9 → 9 >= 7 → aprobados = 2
    #nota=6 → 6 >= 7 → NO cambia

    #resultado: 2 aprobados

n = int(input("¿Cuántos estudiantes? "))
aprobados = 0                       # contador arranca en 0

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:                   # el 7 es el umbral (o 70 si es sobre 100)
        aprobados += 1              # aumenta solo si aprobó

print(f"Aprobados: {aprobados} de {n}")

#Ampliado
    #Bosquejo 
    #n = 3 estudiantes

    #nota 1 = 8   → 8 >= 7  → aprobado   (aprobados=1, reprobados=0)
    #nota 2 = 5   → 5 < 7   → reprobado  (aprobados=1, reprobados=1)
    #nota 3 = 9   → 9 >= 7  → aprobado   (aprobados=2, reprobados=1)

    #porcentaje = (2 / 3) * 100 = 66.6%

n = int(input("¿Cuántos estudiantes? "))
aprobados = 0
reprobados = 0  

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1  

porcentaje_aprobacion = (aprobados / n) * 100 if n > 0 else 0


print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"Porcentaje de aprobación: {porcentaje_aprobacion:.1f}%")