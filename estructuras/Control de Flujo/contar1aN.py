#Taller 3
#IA
    #Bosquejo
    #n = 5

    #for i in range(1, 6):   # 1, 2, 3, 4, 5
    #    print(i)

n = int(input("N: "))

for i in range(1, n + 1):      # ¡ojo con el n+1!
    print(i)

#Ampliado
    #Bosquejo (conteo ascendente)
    #n = 5

    #range(1, 6) genera: 1, 2, 3, 4, 5
    #(el segundo valor no se incluye, por eso es n+1)

n = int(input("N: "))

for i in range(1, n + 1):      # ¡ojo con el n+1!
    print(i)
##
n = int(input("N: "))

for i in range(n, 0, -1):      # ¡ojo con el n+1!
    print(i)