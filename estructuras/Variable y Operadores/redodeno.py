#Ejercicio Propuesto
#IA
num = float(input("Número: "))
dec = int(input("Decimales: "))

# La función round() redondea al entero más cercano
resultado = round(num, dec)
print(resultado)

#Hecho
    #Bosquejo
    #valor = 3.14159, cifras = 2

    #round(3.14159, 2) redondea a 2 decimales → 3.14

valor = float(input("Número: "))
cifras = int(input("Decimales: "))

valor_redondeado = round(valor, cifras)

print(valor_redondeado)