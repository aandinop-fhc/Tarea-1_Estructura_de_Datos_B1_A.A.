#Taller 2
#IA
    #Bosquejo
    #precio = 80
    #iva   = 80 × 0.15 = 12
    #total = 80 + 12   = 92

IVA = 0.15                              # constante en MAYÚSCULA

precio = float(input("Precio sin IVA: $"))
iva = precio * IVA
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}")


#Ampliado
    #Bosquejo
    #precio = 80
    #descuento = 80 × 0.10   = 8
    #precio_con_descuento = 80 - 8 = 72
    #iva   = 72 × 0.15 = 10.8
    #total = 72 + 10.8 = 82.8

IVA = 0.15                              
DESCUENTO = 0.10                       

precio = float(input("Precio sin IVA: $"))

descuento = precio * DESCUENTO
precio_con_descuento = precio - descuento

iva = precio_con_descuento * IVA
total = precio_con_descuento + iva

print(f"Descuento: ${descuento:.2f}")
print(f"IVA:       ${iva:.2f}")
print(f"Total:     ${total:.2f}")