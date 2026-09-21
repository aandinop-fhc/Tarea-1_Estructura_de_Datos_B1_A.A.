#Ejercicio Propuesto
#IA
total = int(input("Segundos totales: "))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas}:{minutos:02d}:{segundos:02d}")

#Hecho
    #Bosquejo
    #total = 3725 segundos

    #Cuántas horas completas hay:
    #  3725 // 3600 = 1 hora
    #Lo que sobra después de esa hora:
    #  3725 % 3600 = 125 segundos

    #De esos 125 segundos, cuántos minutos completos hay:
    #  125 // 60 = 2 minutos
    #Y lo que sobra son los segundos finales:
    #  125 % 60 = 5 segundos
    
    #Resultado: 1:02:05

segundos_totales = int(input("Total de segundos: "))

h = segundos_totales // 3600
sobrante = segundos_totales % 3600

m = sobrante // 60
s = sobrante % 60

resultado = f"{h}:{m:02d}:{s:02d}"
print(resultado)