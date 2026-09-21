            #COMBINADOR DE LISTAS
#IA    
    #Bosquejo
    #intercalar([1,2], [3,4])

    #posición 0: lista1[0]=1, lista2[0]=3 → tomar 1, luego 3
    #posición 1: lista1[1]=2, lista2[1]=4 → tomar 2, luego 4

    #resultado: [1, 3, 2, 4]

class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        largo = min(len(lista1), len(lista2))
        for i in range(largo):
            resultado.append(lista1[i])
            resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        resultado = list(listas[0])
        for i in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[i])
        return resultado


cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))





#13C
    # Bosquejo
        # intercalar(["pan","leche"], ["huevos","queso"]):
        #   posición 0: lista1[0]="pan", lista2[0]="huevos" → tomar "pan", luego "huevos"
        #   posición 1: lista1[1]="leche", lista2[1]="queso" → tomar "leche", luego "queso"
        #   resultado: ["pan","huevos","leche","queso"]

class CombinadorCompras:
    def intercalar(self, lista1, lista2):
        resultado = []
        largo = min(len(lista1), len(lista2))
        for i in range(largo):
            resultado.append(lista1[i])
            resultado.append(lista2[i])
        return resultado


cc = CombinadorCompras()
print(cc.intercalar(["pan", "leche"], ["huevos", "queso"]))