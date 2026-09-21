            #VALIDADOR DE NOTAS CON PROMEDIO
#IA    
    #Bosquejo
    #Notas a cargar: -60, 80, 40, 200

    #¿-60 válida?  -60 < 0        → NO
    #¿80 válida?   0 ≤ 80 ≤ 100   → SÍ  → notas = [80]
    #¿40 válida?   0 ≤ 40 ≤ 100   → SÍ  → notas = [80, 40]
    #¿200 válida?  200 > 100      → NO

    #Lista final: [80, 40]
    #Promedio: (80 + 40) / 2 = 60.0

class Calificador:
    def __init__(self):
        self.notas=[]

    def validar_nota(self,nota):
        if nota >=0 and nota <= 100:
            return True
        else:
            return False
    
    def cargar_notas(self,*args):
        
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas)/len(self.notas)


cal = Calificador()
print(cal.cargar_notas(-30,60,20,120))
print(cal.promedio())




#1E
    #Bosquejo
        #registrar_presiones(50, 90, 200, 120, 75)

        #¿50 válida?
        #  70 <= 50? NO → ya falla
        #  Resultado: NO válida → se descarta

        #¿90 válida?
        #  70 <= 90 <= 180? SÍ
        #  Resultado: válida → presiones = [90]

        #¿200 válida?
        #  200 <= 180? NO
        #  Resultado: NO válida → se descarta

        #¿120 válida?
        #  70 <= 120 <= 180? SÍ
        #  Resultado: válida → presiones = [90, 120]

        #¿75 válida?
        #  70 <= 75 <= 180? SÍ
        #  Resultado: válida → presiones = [90, 120, 75]

        #Lista final: [90, 120, 75]

        #presion_minima():
        #  ¿lista vacía? NO
        #  mínimo entre 90, 120, 75 → 75

class MonitorPresion:
    def __init__(self):
        self.pre = []

    def validar_presion(self, presion):
        if presion >= 70 and presion <= 180:
            return True
        else:
            return False

    def registrar_presiones(self, *presiones):
        for presion in presiones:
            if self.validar_presion (presion):
                self.pre.append(presion)
        return self.pre

    def presion_minima(self):
        if not self.pre:
            return None
        minimo = self.pre [0]
        for presion in self.pre:
            if presion < minimo:
                minimo = presion
        return minimo

mp = MonitorPresion ()
print(mp.registrar_presiones(50, 90, 200, 120, 75))
print(mp.presion_minima())