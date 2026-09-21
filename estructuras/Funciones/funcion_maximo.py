#Ejercicio Propuesto
#IA
def maximo(a, b, c):
    return max(a, b, c)         

# O manualmente:
def maximo_manual(a, b, c):
    mayor = a
    if b > mayor: mayor = b
    if c > mayor: mayor = c
    return mayor

print(maximo(8, 13, 1))          
print(maximo_manual(6, 26, 14))


#Hecho
    #Bosquejo
    #x = 5, y = 9, z = 3

    #mayor = x = 5 (INICIALIZACIÓN)
    #¿y > mayor? → 9 > 5 → sí → mayor = 9
    #¿z > mayor? → 3 > 9 → no → mayor sigue en 9

    #resultado: mayor = 9

def encontrar_mayor(x, y, z):
    mayor = x

    if y > mayor:
        mayor = y

    if z > mayor:
        mayor = z

    return mayor

# Uso
print(encontrar_mayor(5, 9, 3))    # 9
