            #MATRIZ DE DISTANCIA
#IA    
    #Bosquejo
    #distancia_euclidiana((0,0), (3,4)):
    #  diferencia en x: 3 - 0 = 3
    #  diferencia en y: 4 - 0 = 4
    #  distancia = raíz(3² + 4²) = raíz(9 + 16) = raíz(25) = 5.0

    #punto_mas_cercano((0,0), (3,4), (1,1)):
    #  distancia a (3,4): 5.0
    #  distancia a (1,1): raíz(1² + 1²) = raíz(2) ≈ 1.41
    #  ¿cuál es menor? (1,1) con 1.41
    #  resultado: (1,1)

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        mejor_punto = None
        menor_distancia = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                mejor_punto = punto
        return mejor_punto


cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))
print(cd.punto_mas_cercano((0, 0), (3, 4), (1, 1)))





#18D
    # Bosquejo
        # distancia_euclidiana((0,0),(6,8)): raíz((6-0)²+(8-0)²) = raíz(100) = 10.0
        # tienda_mas_cercana: compara distancias, se queda con la menor

class LocalizadorTiendas:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        self.distancias.append(distancia)
        return distancia

    def tienda_mas_cercana(self, referencia, *tiendas):
        mejor_tienda = None
        menor_distancia = None
        for tienda in tiendas:
            distancia = self.distancia_euclidiana(referencia, tienda)
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                mejor_tienda = tienda
        return mejor_tienda


lt = LocalizadorTiendas()
print(lt.distancia_euclidiana((0, 0), (6, 8)))
print(lt.tienda_mas_cercana((0, 0), (6, 8), (2, 2)))