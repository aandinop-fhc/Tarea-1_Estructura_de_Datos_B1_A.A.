#Taller 4
#IA
    #Bosquejo
    #def calcular_iva(precio):
    #   return precio * 0.15

    # Uso
    #iva = calcular_iva(80)   # 12.0
    #imprimo iva              # 12.0

def calcular_iva(precio):
    return precio * 0.15

# --- Programa principal ---
precio = float(input("Precio: $"))
iva = calcular_iva(precio)
print(f"IVA de ${precio}: ${iva:.2f}")

#Ampliado
    #Bosquejo
    #precio = 100

    #calcular_iva(100)   → 100 * 0.15 = 15.0
    #calcular_total(100) → 100 + calcular_iva(100) = 100 + 15.0 = 115.0

def calcular_iva(precio):
    return precio * 0.15

def calcular_total(precio):
    return precio + calcular_iva(precio)

# --- Programa principal ---
precio = float(input("Precio: $"))
iva = calcular_iva(precio)          
total = calcular_total(precio)

print(f"IVA de ${precio}: ${iva:.2f}")
print(f"Total: ${total:.2f}")