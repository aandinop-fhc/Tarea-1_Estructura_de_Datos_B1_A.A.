            #MAPEO DE ESTUDIANTES A NOTAS
#IA    
    #Bosquejo
    #registrar("Ana", 95)
    #  diccionario = {"Ana": 95}

    #registrar("Bob", 70)
    #  diccionario = {"Ana": 95, "Bob": 70}

    #estudiantes_aprobados(80):
    #  ¿Ana (95) >= 80?  Sí → incluir
    #  ¿Bob (70) >= 80?  No → excluir
    #  resultado: ["Ana"]

    #mejor_estudiante():
    #  ¿Ana (95) es mayor al marcador (-1)? Sí → marcador = ("Ana", 95)
    #  ¿Bob (70) es mayor a 95?             No → sigue igual
    #  resultado: ("Ana", 95)

class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)
        return resultado

    def mejor_estudiante(self):
        mejor_nombre = None
        mejor_nota = -1
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
        return (mejor_nombre, mejor_nota)


rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.mejor_estudiante())





#14A
    # Bosquejo
        # registrar("Karla", 88) → puntajes = {"Karla": 88}
        # registrar("Tomas", 65) → puntajes = {"Karla": 88, "Tomas": 65}
        #
        # jugadores_clasificados(70): Karla(88)>=70 sí, Tomas(65)>=70 no → ["Karla"]
        # mejor_jugador(): Karla tiene el puntaje más alto → ("Karla", 88)

class RegistroPuntajes:
    def __init__(self):
        self.puntajes = {}

    def registrar(self, jugador, puntaje):
        self.puntajes[jugador] = puntaje

    def jugadores_clasificados(self, puntaje_minimo):
        resultado = []
        for jugador, puntaje in self.puntajes.items():
            if puntaje >= puntaje_minimo:
                resultado.append(jugador)
        return resultado

    def mejor_jugador(self):
        mejor_nombre = None
        mejor_puntaje = -1
        for jugador, puntaje in self.puntajes.items():
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_nombre = jugador
        return (mejor_nombre, mejor_puntaje)


rp = RegistroPuntajes()
rp.registrar("Karla", 88)
rp.registrar("Tomas", 65)
print(rp.mejor_jugador())