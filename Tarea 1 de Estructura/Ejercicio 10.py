            #GESTOR DE TAREAS CON PRIORIDAD
#IA    
    #Bosquejo
    #agregar_tarea("Estudiar", "alta")
    #  lista = [("Estudiar", "alta")]

    #agregar_tarea("Leer", "baja")
    #  lista = [("Estudiar", "alta"), ("Leer", "baja")]

    #tareas_prioritarias():
    #  ¿("Estudiar","alta") tiene prioridad "alta"?  Sí → incluir
    #  ¿("Leer","baja") tiene prioridad "alta"?      No → excluir
    #  resultado: [("Estudiar", "alta")]

    #eliminar_completada("Estudiar"):
    #  buscar tupla cuya descripción sea "Estudiar" → ("Estudiar","alta")
    #  quitarla de la lista
    #  lista = [("Leer", "baja")]

class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []
        for descripcion, prioridad in self.tareas:
            if prioridad == "alta":
                resultado.append((descripcion, prioridad))
        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break


t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())






#10C
    # Bosquejo
        # agregar_reserva("Mesa 5", "urgente")  → reservas = [("Mesa 5", "urgente")]
        # agregar_reserva("Mesa 2", "normal")   → reservas = [("Mesa 5","urgente"), ("Mesa 2","normal")]
        
        # reservas_urgentes():
        #   ¿("Mesa 5","urgente") es urgente? Sí → incluir
        #   ¿("Mesa 2","normal") es urgente?  No → excluir
        #   resultado: [("Mesa 5","urgente")]
        
        # cancelar_reserva("Mesa 5"): quita la tupla cuyo nombre sea "Mesa 5"
        #   reservas = [("Mesa 2","normal")]

class Reservas:
    def __init__(self):
        self.reservas = []

    def agregar_reserva(self, nombre, prioridad):
        self.reservas.append((nombre, prioridad))

    def reservas_urgentes(self):
        resultado = []
        for nombre, prioridad in self.reservas:
            if prioridad == "urgente":
                resultado.append((nombre, prioridad))
        return resultado

    def cancelar_reserva(self, nombre):
        for reserva in self.reservas:
            if reserva[0] == nombre:
                self.reservas.remove(reserva)
                break


r = Reservas()
r.agregar_reserva("Mesa 5", "urgente")
r.agregar_reserva("Mesa 2", "normal")
print(r.reservas_urgentes())