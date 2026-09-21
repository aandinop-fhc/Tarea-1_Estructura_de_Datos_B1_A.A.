            #SELECTOR DE RANGO CON TUPLAS
#IA    
    #Bosquejo
    #elementos_en_multiples_rangos((1,3), (2,4))

    #crear_rango(1,3):
    #  números desde 1 hasta 3 (incluido) → (1, 2, 3)

    #crear_rango(2,4):
    #  números desde 2 hasta 4 (incluido) → (2, 3, 4)

    #Unir en un conjunto (sin duplicados):
    #  {1,2,3} ∪ {2,3,4} = {1, 2, 3, 4}

    #Convertir a lista ordenada:
    #  [1, 2, 3, 4]

class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        combinados = set()
        for inicio, fin in rangos:
            combinados.update(self.crear_rango(inicio, fin))
        return sorted(combinados)


sr = SelectorRango()
print(sr.crear_rango(1, 3))
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))






#12D
    # Bosquejo
        # crear_turno(8,10) → horas del 8 al 10 → (8, 9, 10)
        # crear_turno(9,11) → (9, 10, 11)
        
        # horas_en_multiples_turnos((8,10),(9,11)):
        #   unir sin duplicados: {8,9,10} y {9,10,11} → {8,9,10,11}
        #   ordenar → [8, 9, 10, 11]

class SelectorTurnos:
    def crear_turno(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def horas_en_multiples_turnos(self, *turnos):
        combinadas = set()
        for inicio, fin in turnos:
            combinadas.update(self.crear_turno(inicio, fin))
        return sorted(combinadas)


st = SelectorTurnos()
print(st.horas_en_multiples_turnos((8, 10), (9, 11)))