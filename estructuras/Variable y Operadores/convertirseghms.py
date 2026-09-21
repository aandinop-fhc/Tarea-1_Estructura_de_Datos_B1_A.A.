#Taller 2
#IA
    #Bosquejo
    #total = 3725 segundos

    #horas    = 3725 // 3600 = 1        sobran 125
    #minutos  = 125  // 60   = 2        sobran 5
    #segundos = 5

    #resultado: 01:02:05
total = int(input("Segundos totales: "))

horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

#Ampliado
    #Bosquejo
    #tiempo = "01:02:05"

    #hh = "01" → 1
    #mm = "02" → 2
    #ss = "05" → 5

    #total = 1×3600 + 2×60 + 5 = 3600 + 120 + 5 = 3725

tiempo = input("Ingresa el tiempo (hh:mm:ss): ")

partes = tiempo.split(":")

hh = int(partes[0])
mm = int(partes[1])
ss = int(partes[2])

total_segundos = hh * 3600 + mm * 60 + ss

print(f"Total en segundos: {total_segundos}")