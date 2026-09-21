            #INVERSOR DE SECUENCIAS
#IA    
    #Bosquejo
    #invertir_lista([1, 2, 3]):
    #  Recorro de atrás hacia adelante:
    #    índice 2 → 3
    #    índice 1 → 2
    #    índice 0 → 1
    #  Resultado: [3, 2, 1]

    #invertir_multiples([1,2,3], [4,5]):
    #  invertir_lista([1,2,3]) → [3, 2, 1]
    #  invertir_lista([4,5])   → [5, 4]
    # Resultado: {(1,2,3): [3,2,1], (4,5): [5,4]}

class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            clave = tuple(lista)          
            resultado[clave] = self.invertir_lista(lista)
        return resultado


inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(inv.invertir_multiples([1, 2, 3], [4, 5]))






#4B
    #Bosquejo
        #triplicar_elementos([5, 9]):
        #  recorro cada elemento y lo agrego tres veces:
        #    elemento 5 → agrego 5, agrego 5, agrego 5
        #    elemento 9 → agrego 9, agrego 9, agrego 9
        #  Resultado: [5, 5, 5, 9, 9, 9]

        #triplicar_multiples([5,9], [2,4,6]):
        #  triplicar_elementos([5,9])   → [5,5,5,9,9,9]
        #  triplicar_elementos([2,4,6]) → [2,2,2,4,4,4,6,6,6]

        #  claves (convertidas a tupla):
        #    (5,9)   → clave
        #    (2,4,6) → clave

        #  Resultado: {(5,9): [5,5,5,9,9,9], (2,4,6): [2,2,2,4,4,4,6,6,6]}

class Triplicador:
    def triplicar_elementos(self,lista):
        ele = []
        for m in lista:
            ele.append(m)
            ele.append(m)
            ele.append(m)
        return ele

    def triplicar_multiples(self, *listas):
        dic = {}
        for lista in listas:
            con = tuple(lista)
            dic [con] = self.triplicar_elementos(lista)
        return dic

tr = Triplicador()
print(tr.triplicar_elementos([5, 9]))
print(tr.triplicar_multiples([5, 9], [2, 4, 6]))
