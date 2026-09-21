#Taller 4
#IA
    #Bosquejo
    #saludar()   → pide nombre, muestra saludo
    #despedir()  → pide nombre, muestra despedida
    #menu()      → muestra opciones y llama a la función correcta

def saludar():
    nombre = input("Nombre: ")
    print(f"¡Hola, {nombre}!")

def despedir():
    nombre = input("Nombre: ")
    print(f"¡Adiós, {nombre}!")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        saludar()
    elif opcion == "2":
        despedir()
    elif opcion == "3":
        print("Adiós")
        break
    else:
        print("Opción inválida")


#Ampliar
def saludar():
    nombre = input("Nombre: ")
    print(f"¡Hola, {nombre}!")

def despedir():
    nombre = input("Nombre: ")
    print(f"¡Adiós, {nombre}!")

    #Bosquejo
    #num1 = 10, num2 = 3

    #suma          = 10 + 3  = 13
    #resta         = 10 - 3  = 7
    #multiplicacion = 10 * 3 = 30
    #division      = 10 / 3  = 3.333...

def calcular():
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 != 0 else "indefinida (división entre 0)"

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Calcular")
    print("4. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        saludar()
    elif opcion == "2":
        despedir()
    elif opcion == "3":
        calcular()
    elif opcion == "4":
        print("Adiós")
        break
    else:
        print("Opción inválida")