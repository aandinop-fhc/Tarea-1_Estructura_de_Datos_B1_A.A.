            #CONTADOR DE FRECUENCIA
#IA    
    #Bosquejo
    #agregar_elemento("a")
    #  diccionario = {"a": 1}

    #agregar_elemento("b")
    #  diccionario = {"a": 1, "b": 1}

    #agregar_elemento("a")   ← ya existe, sube el contador
    #  diccionario = {"a": 2, "b": 1}

    #elemento_mas_frecuente():
    #  ¿"a" tiene 2, "b" tiene 1?
    #  El mayor es "a"

    #frecuencia_elemento("a"):
    #  diccionario["a"] = 2

class ContadorFrecuencia:
    def __init__(self):
        self.conteo = {}

    def agregar_elemento(self, elemento):
        if elemento in self.conteo:
            self.conteo[elemento] += 1
        else:
            self.conteo[elemento] = 1

    def elemento_mas_frecuente(self):
        mayor_elemento = None
        mayor_cantidad = -1
        for elemento, cantidad in self.conteo.items():
            if cantidad > mayor_cantidad:
                mayor_cantidad = cantidad
                mayor_elemento = elemento
        return mayor_elemento

    def frecuencia_elemento(self, elemento):
        return self.conteo.get(elemento, 0)


cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())






#11B
    # Bosquejo
        # agregar_palabra("bueno") → conteo = {"bueno": 1}
        # agregar_palabra("malo")  → conteo = {"bueno": 1, "malo": 1}
        # agregar_palabra("bueno") → conteo = {"bueno": 2, "malo": 1}
        
        # palabra_mas_usada(): "bueno" tiene 2, "malo" tiene 1 → gana "bueno"
        # veces_usada("bueno"): conteo["bueno"] = 2

class ContadorComentarios:
    def __init__(self):
        self.conteo = {}

    def agregar_palabra(self, palabra):
        if palabra in self.conteo:
            self.conteo[palabra] += 1
        else:
            self.conteo[palabra] = 1

    def palabra_mas_usada(self):
        mayor_palabra = None
        mayor_cantidad = -1
        for palabra, cantidad in self.conteo.items():
            if cantidad > mayor_cantidad:
                mayor_cantidad = cantidad
                mayor_palabra = palabra
        return mayor_palabra

    def veces_usada(self, palabra):
        return self.conteo.get(palabra, 0)


cc = ContadorComentarios()
cc.agregar_palabra("bueno")
cc.agregar_palabra("malo")
cc.agregar_palabra("bueno")
print(cc.palabra_mas_usada())