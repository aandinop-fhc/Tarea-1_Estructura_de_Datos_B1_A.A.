#Ejercicio Propuesto
#IA
precio = float(input("Precio sin IVA: $"))
iva = precio * 0.15
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}")

#Hecho
    #Bosquejo
    #precio_producto = 100

    #IVA   = 100 × 0.15 = 15.00
    #total = 100 + 15   = 115.00

precio_producto = float(input("Precio del producto: $"))

valor_iva = precio_producto * 0.15
precio_final = precio_producto + valor_iva

print(f"IVA: ${valor_iva:.2f}")
print(f"Total: ${precio_final:.2f}")