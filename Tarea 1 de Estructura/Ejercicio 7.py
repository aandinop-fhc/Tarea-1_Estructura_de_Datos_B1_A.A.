            #MAPEADO DE EDADES
#IA    
    #Bosquejo
    #agregar_persona("Ana", 28)
    #  diccionario = {"Ana": 28}

    #agregar_persona("Bob", 17)
    #  diccionario = {"Ana": 28, "Bob": 17}

    #personas_mayores(18):
    #  ¿Ana (28) >= 18?  Sí → incluir
    #  ¿Bob (17) >= 18?  No → excluir
    #  resultado: ["Ana"]

    #edad_promedio():
    #  (28 + 17) / 2 = 22.5

class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))
print(gp.edad_promedio())






#7A
    #Bosquejo
        #registrar_empleado("Marta", 40)
        #  empleados = {"Marta": 40}

        #registrar_empleado("Iván", 20)
        #  empleados = {"Marta": 40, "Iván": 20}

        #registrar_empleado("Cindy", 35)
        #  empleados = {"Marta": 40, "Iván": 20, "Cindy": 35}

        #empleados_tiempo_completo(30):
        #  ¿Marta (40) >= 30?  Sí → incluir
        #  ¿Iván (20) >= 30?   No → excluir
        #  ¿Cindy (35) >= 30?  Sí → incluir
        #  resultado: ["Marta", "Cindy"]

        #horas_promedio():
        #  (40 + 20 + 35) / 3 = 95 / 3 = 31.666...

class ControlHoras:
    def __init__(self):
        self.tiempo = {}

    def registrar_empleado(self, nombre, horas):
        self.tiempo [nombre] = horas

    def empleados_tiempo_completo(self, horas_minimas):
        h = []
        for nombre, horas in self.tiempo.items():
            if horas >= horas_minimas:
                h.append(nombre)
        return h

    def horas_promedio(self):
        if not self.tiempo:
            return 0
        return sum(self.tiempo.values()) / len(self.tiempo)

ch = ControlHoras()
ch.registrar_empleado("Marta", 40)
ch.registrar_empleado("Iván", 20)
ch.registrar_empleado("Cindy", 35)
print(ch.empleados_tiempo_completo(30))
print(ch.horas_promedio())