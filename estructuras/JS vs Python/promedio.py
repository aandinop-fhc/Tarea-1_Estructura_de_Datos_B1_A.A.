#Taller 1
#IA
    #Bosquejo
    # n1 = 8, n2 = 6, n3 = 10
    # paso 1: sumo    8 + 6 + 10 = 24
    # paso 2: divido  24 / 3     = 8.0
    # paso 3: muestro "Promedio: 8.0"

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3      # PROCESO en una línea

print(f"Promedio: {promedio:.1f}")  # :.1f muestra un decimal


#Ampliado
    #Bosquejo
    # n1 = 9, n2 = 5, n3 = 8
    # paso 1: sumo    9 + 5 + 8 = 22
    # paso 2: divido  22 / 3     = 8.33
    # paso 3: muestro "Promedio: 7.33""Aprobado"
    
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3      # PROCESO en una línea
if promedio >=7.0:
    print("Aprobado")
else:  
    print("Reprobado")  
print(f"Promedio: {promedio:.2f}")  # :.2f muestra un decimal5
