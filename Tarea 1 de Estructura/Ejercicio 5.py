            #DETECTOR DE NÚMEROS PARES E IMPARES
#IA    
    #Bosquejos
    #separar(1, 2, 3, 4, 5)

    #es_par(1) → 1 % 2 = 1 → No es par → impar
    #es_par(2) → 2 % 2 = 0 → Sí es par
    #es_par(3) → 3 % 2 = 1 → impar
    #es_par(4) → 4 % 2 = 0 → par
    #es_par(5) → 5 % 2 = 1 → impar

    #diccionario = {'pares': [2, 4], 'impares': [1, 3, 5]}

    #cantidad_pares_impares():
    #  cant_pares = len([2,4]) = 2
    #  cant_impares = len([1,3,5]) = 3
    #  resultado: (2, 3)

class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {'pares': self.pares, 'impares': self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())






#5B
    #Bosquejo
        #clasificar_visitantes(15, 22, 17, 40, 12)

        #es_mayor_edad(15) → 15 >= 18? NO → menor
        #es_mayor_edad(22) → 22 >= 18? SÍ → adulto
        #es_mayor_edad(17) → 17 >= 18? NO → menor
        #es_mayor_edad(40) → 40 >= 18? SÍ → adulto
        #es_mayor_edad(12) → 12 >= 18? NO → menor

        #adultos = [22, 40]
        #menores = [15, 17, 12]

        #cantidad_por_grupo():
        #  cant_adultos = len([22,40]) = 2
        #  cant_menores = len([15,17,12]) = 3
        #  resultado: (2, 3)

class ControlAcceso:
    def __init__(self):
        self.adultos = []
        self.menores = []

    def es_mayor_edad(self, edad):
        if edad >= 18:
            return True
        else:
            return False

    def clasificar_visitantes (self, *edades):
        for edad in edades:
            if self.es_mayor_edad (edad):
                self.adultos.append(edad)
            else:
                self.menores.append(edad)
        return {"adultos":self.adultos, "menores":self.menores}

    def cantidad_por_grupo (self):
        return (len(self.adultos), len(self.menores))

ca = ControlAcceso()
print(ca.clasificar_visitantes(15, 22, 17, 40, 12))
print(ca.cantidad_por_grupo())