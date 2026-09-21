#Ejercicio Propuesto
#IA
notas = [6,9.5,8,5,3.6,10]
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Máximo:   {max(notas):.2f}")
print(f"Mínimo:   {min(notas):.2f}")


#Hecho
    #Bosquejo
    #calificaciones = [7, 8.5, 6, 9, 10, 5.5]

    #suma_total = 7+8.5+6+9+10+5.5 = 46
    #cantidad = 6
    #promedio = 46 / 6 = 7.666...

    #nota_mayor = 10
    #nota_menor = 5.5

calificaciones = [7, 8.5, 6, 9, 10, 5.5]

suma_total = sum(calificaciones)
cantidad = len(calificaciones)
promedio = suma_total / cantidad

nota_mayor = max(calificaciones)
nota_menor = min(calificaciones)

print(f"Promedio: {promedio:.2f}")
print(f"Máximo:   {nota_mayor:.2f}")
print(f"Minimo:   {nota_menor:.2f}")