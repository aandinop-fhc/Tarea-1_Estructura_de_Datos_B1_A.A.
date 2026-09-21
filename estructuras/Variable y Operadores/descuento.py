#Ejercicio Propuesto
#IA
PRECIO = 12
cant = int(input("Cantidad: "))

# Determinar el descuento
if cant >= 10:
    descuento = 0.15
elif cant >= 5:
    descuento = 0.05
else:
    descuento = 0

subtotal = PRECIO * cant
total = subtotal * (1 - descuento)

print(f"Precio unitario: ${PRECIO}")
print(f"Descuento: {int(descuento*100)}%")
print(f"Total: ${total:.2f}")

#Hecho
    #Bosquejo
    #cantidad = 12, precio_unitario = 12

    #subtotal = 12 × 12 = 144
    #rebaja = 144 × 0.15 = 21.6
    #total = 144 - 21.6 = 122.4

PRECIO_UNITARIO = 12

cantidad = int(input("Cantidad: "))

if cantidad >= 10:
    porcentaje = 15
elif cantidad >= 5:
    porcentaje = 5
else:
    porcentaje = 0

subtotal = PRECIO_UNITARIO * cantidad
rebaja = subtotal * porcentaje / 100
total = subtotal - rebaja

print(f"Precio unitario: ${PRECIO_UNITARIO}")
print(f"Descuento: {porcentaje}%")
print(f"Total: ${total:.2f}")

