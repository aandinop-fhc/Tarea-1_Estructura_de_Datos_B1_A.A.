            #ASIGNADOR DE EQUIPOS
#IA    
    #Bosquejo
    #crear_equipo("A")
    #  diccionario = {"A": []}

    #agregar_jugador("A", "Juan")
    #  diccionario = {"A": ["Juan"]}

    #agregar_jugador("A", "Pedro")
    #  diccionario = {"A": ["Juan", "Pedro"]}

    #crear_equipo("B")
    #  diccionario = {"A": ["Juan","Pedro"], "B": []}

    #agregar_jugador("B", "Luis")
    #  diccionario = {"A": ["Juan","Pedro"], "B": ["Luis"]}

    #equipo_mayor_integrantes():
    #  ¿"A" tiene cuántos? 2
    #  ¿"B" tiene cuántos? 1
    #  El mayor es "A"

class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor_nombre = None
        mayor_cantidad = -1
        for nombre, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                mayor_nombre = nombre
        return mayor_nombre


eq = Equipos()
eq.crear_equipo("A")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.crear_equipo("B")
eq.agregar_jugador("B", "Luis")
print(eq.equipo_mayor_integrantes())






#8B
    #Bosquejo
        # crear_departamento("Ventas")
        #   departamentos = {"Ventas": []}
        #
        # agregar_empleado("Ventas", "Carla")
        #   departamentos = {"Ventas": ["Carla"]}
        #
        # agregar_empleado("Ventas", "Diego")
        #   departamentos = {"Ventas": ["Carla", "Diego"]}
        #
        # crear_departamento("TI")
        #   departamentos = {"Ventas": ["Carla","Diego"], "TI": []}
        #
        # agregar_empleado("TI", "Marco")
        #   departamentos = {"Ventas": ["Carla","Diego"], "TI": ["Marco"]}
        #
        # departamento_mas_grande():
        #   ¿"Ventas" tiene cuántos? 2
        #   ¿"TI" tiene cuántos? 1
        #   El mayor es "Ventas"

class Departamentos:
    def __init__(self):
        self.departamento = {}

    def crear_departamento (self, nombre_depto):
        self.departamento[nombre_depto]=[]

    def agregar_empleado(self, depto, empleado):
        self.departamento[depto].append(empleado)

    def departamento_mas_grande(self):
        mayor_dep = None
        mayor_cantidad = -1
        for depto, empleado in self.departamento.items:
            if len(empleado) > mayor_cantidad:
                mayor_cantidad = len(empleado)
                mayor_dep = depto
        return mayor_dep

d = Departamentos()
d.crear_departamento("Ventas")
d.agregar_empleado("Ventas", "Carla")
d.agregar_empleado("Ventas", "Diego")
d.crear_departamento("TI")
d.agregar_empleado("TI", "Marco")
print(d.departamento_mas_grande())
