            #ANALIZADOR DE PATRONES EN TEXTOS
#IA    
    #Bosquejo
    #texto = "el gato está aquí"

    #split(): separa por espacios → ["el", "gato", "está", "aquí"]

    #encontrar_palabras(texto, "a"):
    #  ¿"el" empieza con "a"?    No
    #  ¿"gato" empieza con "a"?  No
    #  ¿"está" empieza con "a"?  No
    #  ¿"aquí" empieza con "a"?  Sí → incluir
    #  resultado: ["aquí"]

    #agrupar_por_longitud(texto):
    #  "el"   → longitud 2
    #  "gato" → longitud 4
    #  "está" → longitud 4  (e,s,t,á = 4 caracteres)
    #  "aquí" → longitud 4  (a,q,u,í = 4 caracteres)
    #  resultado: {2: ['el'], 4: ['gato', 'está', 'aquí']}

    #palabras_unicas():
    #  conjunto de todas las palabras vistas hasta ahora, sin repetir

class AnalizadorPatrones:
    def __init__(self):
        self.vistas = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            self.vistas.add(palabra)
            if palabra.startswith(patron):
                resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        grupos = {}
        for palabra in palabras:
            self.vistas.add(palabra)
            longitud = len(palabra)
            if longitud in grupos:
                grupos[longitud].append(palabra)
            else:
                grupos[longitud] = [palabra]
        return grupos

    def palabras_unicas(self):
        return self.vistas


ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato está aquí"))





#20C
    # Bosquejo
        # split(): "el servicio fue excelente hoy" → ["el","servicio","fue","excelente","hoy"]
        # encontrar_palabras(texto,"e"): "el","excelente" empiezan con "e" → ["el","excelente"]
        # agrupar_por_longitud: {2:['el'], 8:['servicio'], 3:['fue'], 10:['excelente'], 3:['hoy']}

class AnalizadorComentarios:
    def __init__(self):
        self.vistas = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            self.vistas.add(palabra)
            if palabra.startswith(patron):
                resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        grupos = {}
        for palabra in palabras:
            self.vistas.add(palabra)
            longitud = len(palabra)
            if longitud in grupos:
                grupos[longitud].append(palabra)
            else:
                grupos[longitud] = [palabra]
        return grupos

    def palabras_unicas(self):
        return self.vistas


ac = AnalizadorComentarios()
print(ac.agrupar_por_longitud("el servicio fue excelente hoy"))