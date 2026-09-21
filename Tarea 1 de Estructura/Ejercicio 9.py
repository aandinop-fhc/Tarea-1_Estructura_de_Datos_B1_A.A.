            #VALIDADOR DE CARACTERES
#IA    
    #Bosquejo
    #contar_por_tipo("Hola123")

    #H → ¿vocal? No → ¿dígito? No → consonante
    #o → ¿vocal? Sí → vocal
    #l → ¿vocal? No → ¿dígito? No → consonante
    #a → ¿vocal? Sí → vocal
    #1 → ¿dígito? Sí → dígito
    #2 → ¿dígito? Sí → dígito
    #3 → ¿dígito? Sí → dígito

    #Conteo final:
    #  vocales = 2   (o, a)
    #  consonantes = 2   (H, l)
    #  digitos = 3   (1, 2, 3)

    #Resultado: {'vocales':2, 'consonantes':2, 'digitos':3}

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        vocales = 0
        consonantes = 0
        digitos = 0

        for caracter in texto:
            if caracter.isdigit():
                digitos += 1
            elif self.solo_vocales(caracter):
                vocales += 1
            elif caracter.isalpha():
                consonantes += 1

        return {'vocales': vocales, 'consonantes': consonantes, 'digitos': digitos}


astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))






#9C
    # Bosquejo
        # contar_tipos("Clave123")
        
        # C → ¿mayúscula? Sí → mayúscula
        # l → ¿mayúscula? No → ¿número? No → minúscula
        # a → ¿mayúscula? No → ¿número? No → minúscula
        # v → ¿mayúscula? No → ¿número? No → minúscula
        # e → ¿mayúscula? No → ¿número? No → minúscula
        # 1 → ¿número? Sí → número
        # 2 → ¿número? Sí → número
        # 3 → ¿número? Sí → número
        
        # Conteo final:
        #   mayusculas = 1   (C)
        #   minusculas = 4   (l, a, v, e)
        #   numeros = 3      (1, 2, 3)
        
        # Resultado: {'mayusculas':1, 'minusculas':4, 'numeros':3}

class ValidadorContrasena:
    def __init__(self):
        self.mas_larga = ""

    def es_mayuscula(self, letra):
        return letra.isupper()

    def contar_tipos(self, texto):
        if len(texto) > len(self.mas_larga):
            self.mas_larga = texto

        mayusculas = 0
        minusculas = 0
        numeros = 0

        for caracter in texto:
            if caracter.isdigit():
                numeros += 1
            elif self.es_mayuscula(caracter):
                mayusculas += 1
            elif caracter.isalpha():
                minusculas += 1

        return {'mayusculas': mayusculas, 'minusculas': minusculas, 'numeros': numeros}


vc = ValidadorContrasena()
print(vc.contar_tipos("Clave123"))