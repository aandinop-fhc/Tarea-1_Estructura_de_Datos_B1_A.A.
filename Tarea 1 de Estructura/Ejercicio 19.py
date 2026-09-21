            #INVENTARIO DE PRODUCTOS
#IA    
    #Bosquejo
    #agregar_stock("pan", 50)
    #  diccionario = {"pan": 50}

    #restar_stock("pan", 30):
    #  ¿hay al menos 30 de "pan"? 50 >= 30 → Sí
    #  nuevo stock: 50 - 30 = 20
    #  diccionario = {"pan": 20}
    #  resultado: True

    #productos_bajo_stock(15):
    #  ¿"pan" (20) < 15?  No → no incluir
    #  resultado: []

    #  (nota: en el ejemplo de la guía dice ["pan"], pero con
    #   20 unidades no sería < 15 — puede que el ejemplo de la guía
    #   tenga un valor distinto en mente; sigo la lógica correcta
    #   del enunciado: cantidad < minimo)

class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado


inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.productos_bajo_stock(15))





#19B
    # Bosquejo
        # agregar_medicamento("Paracetamol", 100) → stock = {"Paracetamol": 100}
        # despachar("Paracetamol", 40): hay suficiente (100>=40) → stock = {"Paracetamol": 60} → True
        # medicamentos_bajo_stock(50): 60 no es <50 → []

class Farmacia:
    def __init__(self):
        self.stock = {}

    def agregar_medicamento(self, nombre, cantidad):
        if nombre in self.stock:
            self.stock[nombre] += cantidad
        else:
            self.stock[nombre] = cantidad

    def despachar(self, nombre, cantidad):
        if nombre in self.stock and self.stock[nombre] >= cantidad:
            self.stock[nombre] -= cantidad
            return True
        return False

    def medicamentos_bajo_stock(self, minimo):
        resultado = []
        for nombre, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(nombre)
        return resultado


f = Farmacia()
f.agregar_medicamento("Paracetamol", 100)
print(f.despachar("Paracetamol", 40))
print(f.medicamentos_bajo_stock(50))