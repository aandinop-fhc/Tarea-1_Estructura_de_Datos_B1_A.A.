            #GRUPO DE EDADES
#IA    
    #Bosquejo
    #agrupar_por_categoria(5, 15, 30, 70)

    #clasificar_edad(5):
    #  ¿menor de 13? Sí → "niño"

    #clasificar_edad(15):
    #  ¿menor de 13? No → ¿menor de 18? Sí → "adolescente"

    #clasificar_edad(30):
    #  ¿menor de 13? No → ¿menor de 18? No → ¿menor de 65? Sí → "adulto"

    #clasificar_edad(70):
    #  ¿menor de 13? No → ¿menor de 18? No → ¿menor de 65? No → "mayor"

    #Resultado:
    #  {'niño':[5], 'adolescente':[15], 'adulto':[30], 'mayor':[70]}

    #edad_promedio_categoria("adulto"):
    #  lista de esa categoría: [30]
    #  promedio = 30/1 = 30.0

class AgrupadorEdades:
    def __init__(self):
        self.grupos = {'niño': [], 'adolescente': [], 'adulto': [], 'mayor': []}

    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        lista = self.grupos[categoria]
        if not lista:
            return 0
        return sum(lista) / len(lista)


ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto"))






#17B
    # Bosquejo
        # clasificar_talla(30): <34 → "chica"
        # clasificar_talla(36): <38 → "mediana"
        # clasificar_talla(40): <44 → "grande"
        # clasificar_talla(50): resto → "extra grande"
        
        # agrupar_por_talla(30,36,40,50):
        #   {'chica':[30], 'mediana':[36], 'grande':[40], 'extra grande':[50]}

class AgrupadorTallas:
    def __init__(self):
        self.grupos = {'chica': [], 'mediana': [], 'grande': [], 'extra grande': []}

    def clasificar_talla(self, medida):
        if medida < 34:
            return "chica"
        elif medida < 38:
            return "mediana"
        elif medida < 44:
            return "grande"
        else:
            return "extra grande"

    def agrupar_por_talla(self, *medidas):
        for medida in medidas:
            categoria = self.clasificar_talla(medida)
            self.grupos[categoria].append(medida)
        return self.grupos


at = AgrupadorTallas()
print(at.agrupar_por_talla(30, 36, 40, 50))