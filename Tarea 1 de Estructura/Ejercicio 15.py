            #DIVISORES DE UN NÚMERO
#IA    
    #Bosquejo
    #encontrar_divisores(12):
    #  ¿1 divide a 12?  12 % 1 = 0 → sí
    #  ¿2 divide a 12?  12 % 2 = 0 → sí
    #  ¿3 divide a 12?  12 % 3 = 0 → sí
    #  ¿4 divide a 12?  12 % 4 = 0 → sí
    #  ¿5 divide a 12?  12 % 5 = 2 → no
    #  ¿6 divide a 12?  12 % 6 = 0 → sí
    #  ...
    #  ¿12 divide a 12? 12 % 12 = 0 → sí
    #  resultado: (1, 2, 3, 4, 6, 12)

    #es_perfecto(12):
    #  divisores sin contar el 12 mismo: 1,2,3,4,6
    #  suma = 1+2+3+4+6 = 16
    #  ¿16 == 12? No → False (12 NO es perfecto)

    #  (dato aparte: 6 SÍ sería perfecto porque 1+2+3=6)

    #encontrar_multiples_divisores(12, 6):
    #  {12: (1,2,3,4,6,12), 6: (1,2,3,6)}

class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = sum(divisores) - numero   # se resta el número mismo
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado


df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(6))





#15C
    # Bosquejo
        # encontrar_multiplos(4, 20): 4,8,12,16,20 son múltiplos de 4 hasta 20 → (4,8,12,16,20)
        # suma_multiplos(4, 20): 4+8+12+16+20 = 60

class MultiploFinder:
    def encontrar_multiplos(self, base, limite):
        multiplos = []
        for i in range(base, limite + 1):
            if i % base == 0:
                multiplos.append(i)
        return tuple(multiplos)

    def suma_multiplos(self, base, limite):
        multiplos = self.encontrar_multiplos(base, limite)
        return sum(multiplos)


mf = MultiploFinder()
print(mf.encontrar_multiplos(4, 20))
print(mf.suma_multiplos(4, 20))