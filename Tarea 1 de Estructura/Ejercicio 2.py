            #CONTADOR DE PALABRAS ÚNICAS
#IA    
    #Bosquejo
    #agregar_multiples("hola", "mundo", "hola")

    #agregar_palabra("hola"):
    #  conjunto = {"hola"}
    #  lista    = ["hola"]

    #agregar_palabra("mundo"):
    #  conjunto = {"hola", "mundo"}
    #  lista    = ["hola", "mundo"]

    #agregar_palabra("hola"):  <- ya está en el conjunto
    #  conjunto = {"hola", "mundo"}   (no cambia, sets no repiten)
    #  lista    = ["hola", "mundo", "hola"]   (la lista SÍ la vuelve a guardar)

    #contar_palabras():
    #  len(conjunto) = 2


class AnalizadorTexto:
    def __init__(self):
        self.unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        self.unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())





#2B
    #Bosquejo
        #reproducir_multiples("Bohemian Rhapsody", "Imagine", "Bohemian Rhapsody", "Hey Jude")

        #reproducir_cancion("Bohemian Rhapsody"):
        #  distintas = {"Bohemian Rhapsody"}
        #  historial = ["Bohemian Rhapsody"]

        #reproducir_cancion("Imagine"):
        #  distintas = {"Bohemian Rhapsody", "Imagine"}
        #  historial = ["Bohemian Rhapsody", "Imagine"]

        #reproducir_cancion("Bohemian Rhapsody"):  ← ya está en el conjunto
        #  distintas = {"Bohemian Rhapsody", "Imagine"}                      (no cambia)
        #  historial = ["Bohemian Rhapsody", "Imagine", "Bohemian Rhapsody"] (sí se repite)

        #reproducir_cancion("Hey Jude"):
        #  distintas = {"Bohemian Rhapsody", "Imagine", "Hey Jude"}
        #  historial = ["Bohemian Rhapsody", "Imagine", "Bohemian Rhapsody", "Hey Jude"]

        #canciones_distintas():
        #  len(distintas) = 3

class ReproductorMusica:
    def __init__(self):
        self.dis = set ()
        self.his = []

    def reproducir_cancion (self, titulo):
        self.dis.add (titulo)
        self.his.append (titulo)

    def canciones_distintas(self):
        return len(self.dis)

    def reproducir_multiples(self, *titulos):
        for titulo in titulos:
            self.reproducir_cancion (titulo)

rm = ReproductorMusica ()
rm.reproducir_multiples ("Bohemian Rhapsody", "Imagine", "Bohemian Rhapsody", "Hey Jude")
print(rm.canciones_distintas())
