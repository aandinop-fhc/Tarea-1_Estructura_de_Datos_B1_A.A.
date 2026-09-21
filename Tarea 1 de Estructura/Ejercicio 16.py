            #CODIFICADOR/DECODIFICADOR
#IA    
    #Bosquejo
    #codificar_letra("h", 3):
    #  posición de "h" en el alfabeto (a=0, b=1, ..., h=7): 7
    #  desplazar: (7 + 3) % 26 = 10
    #  letra en posición 10: "k"
    #  resultado: "k"

    #codificar_letra("o", 3):
    #  posición de "o": 14
    #  (14 + 3) % 26 = 17 → "r"

    #codificar_letra("l", 3):
    #  posición de "l": 11
    #  (11 + 3) % 26 = 14 → "o"

    #codificar_letra("a", 3):
    #  posición de "a": 0
    #  (0 + 3) % 26 = 3 → "d"

    #codificar_palabra("hola", 3):
    #  une letra por letra: "k"+"r"+"o"+"d" = "krod"

    #  (la guía dice "kroc" pero es un valor aproximado de ejemplo;
    #   la fórmula real del Cifrado César da "krod")

class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        posicion = ord(letra) - ord('a')
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(nueva_posicion + ord('a'))

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = resultado
        return resultado


cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))





#16D
    # Bosquejo
        # codificar_letra("m", 2): posición de m=12, (12+2)%26=14 → letra "o"
        # codificar_mensaje("mar", 2): concatena letra por letra → "oct"

class CodificadorSecreto:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        posicion = ord(letra) - ord('a')
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(nueva_posicion + ord('a'))

    def codificar_mensaje(self, mensaje, desplazamiento):
        resultado = ""
        for letra in mensaje:
            resultado += self.codificar_letra(letra, desplazamiento)
        self.historial[mensaje] = resultado
        return resultado


cs = CodificadorSecreto()
print(cs.codificar_mensaje("mar", 2))