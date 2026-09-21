#Taller 3
#IA
    #Bosquejo
    #n = 5, suma = 0 (INICIALIZACIÓN)

    #i=1:  suma = 0 + 1 = 1
    #i=2:  suma = 1 + 2 = 3
    #i=3:  suma = 3 + 3 = 6
    #i=4:  suma = 6 + 4 = 10
    #i=5:  suma = 10 + 5 = 15   ← resultado

n = int(input("N: "))
suma = 0                    # INICIALIZACIÓN del acumulador

for i in range(1, n + 1):
    suma = suma + i         # equivale a: suma += i

print(f"Suma: {suma}")

#Ampliado
    #Bosquejo

    #i=2:  suma = 0 + 2 = 2
    #i=4:  suma = 2 + 4 = 6
    #i=6:  suma = 6 + 6 = 12
    #...
    #i=100: suma = (acumulado) + 100 → resultado final

suma = 0                          
for i in range(2, 101, 2):
    suma = suma + i                

print(f"Suma: {suma}")