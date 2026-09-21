            #GESTOR DE COMPRAS CON TOTALES
#IA    
    #Bosquejo
    #agregar_articulo("pan", 2.50)
    #  diccionario = {"pan": 2.50}

    #agregar_articulo("leche", 3.00)
    #  diccionario = {"pan": 2.50, "leche": 3.00}

    #total_carrito():
    #  sumar valores → 2.50 + 3.00 = 5.50

    #articulos_por_rango(2, 3):
    #  ¿pan (2.50) está entre 2 y 3?    Sí → incluir
    #  ¿leche (3.00) está entre 2 y 3?  Sí → incluir
    #  resultado: ["pan", "leche"]

class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado


c = CarroCompras()
c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
print(c.total_carrito())
print(c.articulos_por_rango(2, 3))




#3D
    #Bosquejo
        #agregar_cliente("Sofía", 45)
        #  clientes = {"Sofía": 45}

        #agregar_cliente("Pedro", 320)
        #  clientes = {"Sofía": 45, "Pedro": 320}

        #agregar_cliente("Lucía", 150)
        #  clientes = {"Sofía": 45, "Pedro": 320, "Lucía": 150}

        #total_ventas():
        #  sumar valores → 45 + 320 + 150 = 515

        #clientes_por_rango(100, 200):
        #  ¿Sofía (45) está entre 100 y 200?    No → excluir
        #  ¿Pedro (320) está entre 100 y 200?   No → excluir
        #  ¿Lucía (150) está entre 100 y 200?   Sí → incluir
        #  resultado: ["Lucía"]

class TiendaOnline:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente (self, nombre, monto_comprado):
        self.clientes[nombre] = monto_comprado

    def total_ventas(self):
        return sum(self.clientes.values())

    def clientes_por_rango(self, monto_min, monto_max):
        nom = []
        for nombre, monto_comprado in self.clientes.items():
            if monto_min <= monto_comprado <= monto_max:
                nom.append(nombre)
        return nom

to = TiendaOnline()
to.agregar_cliente("Sofía", 45)
to.agregar_cliente("Pedro", 320)
to.agregar_cliente("Lucía", 150)
print(to.total_ventas())
print(to.clientes_por_rango(100, 200))