#Taller 1
#IA
    #Bosquejo
    #base = 5, altura = 3

    #área      = 5 × 3 = 15
    #perímetro = 2 × (5 + 3) = 16

base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura                # PROCESO 1
perimetro = 2 * (base + altura)     # PROCESO 2

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")


#Ampliado
import math

    #Bosquejo (rectángulo)
    #base = 5, altura = 3

    #área      = 4 × 3 = 12
    #perímetro = 2 × (4 + 3) = 14

base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura                # PROCESO 1
perimetro = 2 * (base + altura)     # PROCESO 2

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")


    #Bosquejo (círculo)
    #radio = 4

    #área      = π × 4² ≈ 50.27
    #perímetro = 2 × π × 4 ≈ 25.13

radio = float(input("Radio: "))

area_circulo = math.pi * radio ** 2       # PROCESO 3
perimetro_circulo = 2 * math.pi * radio   # PROCESO 4

print(f"Área del círculo: {area_circulo:.2f}")
print(f"Perímetro del círculo: {perimetro_circulo:.2f}")