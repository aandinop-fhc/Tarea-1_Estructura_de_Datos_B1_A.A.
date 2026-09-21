#Ejercicio Propuesto
#IA
total = int(input("Minutos totales: "))

horas = total // 60
mins = total % 60

print(f"{horas} horas {mins} minutos")

#Hecho
    #Bosquejo
#minutos_totales = 135
#sobrante = 135 % 60 = 15

#divido lo que queda entre 60:
#(135 - 15) // 60 = 120 // 60 = 2

minutos_totales = int(input("Minutos totales: "))

sobrante = minutos_totales % 60
completos = minutos_totales - sobrante

horas = completos // 60

print(f"{horas} horas {sobrante} minutos")