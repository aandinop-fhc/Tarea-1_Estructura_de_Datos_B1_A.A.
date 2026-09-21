            #ESTADISTICA DE TEMPERATURA
#IA    
    #Bosquejo
    #registrar_multiples(20, 25, 18, 30)
    #  lista = [20, 25, 18, 30]

    #minima():
    #  el más chico entre 20, 25, 18, 30 → 18

    #maxima():
    #  el más grande entre 20, 25, 18, 30 → 30

    #promedio():
    #  (20 + 25 + 18 + 30) / 4 = 93 / 4 = 23.25

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())
print(gt.minima())
print(gt.maxima())






#6D
    #Bosquejo
        #registrar_multiples(45, 38, 52, 41)
        #  tiempos = [45, 38, 52, 41]

        #tiempo_minimo():
        #  el más chico entre 45, 38, 52, 41 → 38

        #tiempo_maximo():
        #  el más grande entre 45, 38, 52, 41 → 52

        #promedio_tiempo():
        #  (45 + 38 + 52 + 41) / 4 = 176 / 4 = 44.0

class EstadisticasCarrera:
    def __init__(self):
        self.tiemp = []

    def registrar_tiempo(self, segundos):
        self.tiemp.append(segundos)

    def registrar_multiples(self, *tiempos):
        for segundos in tiempos:
            self.registrar_tiempo(segundos)

    def tiempo_minimo(self):
        if not self.tiemp:
            return None
        mini = self.tiemp[0]
        for segundos in self.tiemp:
            if segundos < mini:
                mini = segundos
        return mini 

    def tiempo_maximo(self):
        if not self.tiemp:
            return None
        maxi = self.tiemp[0]
        for segundos in self.tiemp:
            if segundos > maxi:
                maxi = segundos
        return maxi

    def promedio_tiempo(self):
        if not self.tiemp:
            return 0
        return sum(self.tiemp) / len(self.tiemp)

ecar = EstadisticasCarrera()
ecar.registrar_multiples(45, 38, 52, 41)
print(ecar.tiempo_minimo())
print(ecar.tiempo_maximo())
print(ecar.promedio_tiempo())
    
        
        