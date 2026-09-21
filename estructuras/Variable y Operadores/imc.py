#Ejercicio Propuesto
#IA
peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))

imc = peso / (estatura ** 2)
print(f"IMC: {imc:.2f}")

#Hecho
    #Bosquejo
    #peso = 70, estatura = 1.75

    #estatura_cuadrada = 1.75 × 1.75 = 3.0625
    #imc = 70 / 3.0625 = 22.857...

peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))

estatura_cuadrada = estatura * estatura
imc = peso / estatura_cuadrada

print(f"IMC: {imc:.2f}")