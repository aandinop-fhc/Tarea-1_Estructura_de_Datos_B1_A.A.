#Ejercicio Propuesto
#IA
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return None            # None = "no válido"
    return a / b

while True:
    print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
    op = input("Opción: ")
    if op == "5":
        break
    a = float(input("a: "))
    b = float(input("b: "))
    if op == "1": r = sumar(a, b)
    elif op == "2": r = restar(a, b)
    elif op == "3": r = multiplicar(a, b)
    elif op == "4":
        r = dividir(a, b)
        if r is None:
            print("No se puede dividir entre 0")
            continue
    else:
        print("Opción inválida"); continue
    print(f"Resultado: {r}")


#Hecho
    #Bosquejo
    #op = "1", num1 = 8, num2 = 3

    #operaciones["1"] = sumar → sumar(8, 3) = 11

    #Si op = "4" (dividir) y num2 = 0:
    #dividir(8, 0) → retorna None → mostrar mensaje de error

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return None               
    return num1 / num2

operaciones = {
    "1": sumar,
    "2": restar,
    "3": multiplicar,
    "4": dividir
}

continuar = True

while continuar:
    print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
    op = input("Opción: ")

    if op == "5":
        continuar = False
    elif op in operaciones:
        num1 = float(input("a: "))
        num2 = float(input("b: "))

        resultado = operaciones[op](num1, num2)

        if resultado is None:
            print("No se puede dividir entre 0")
        else:
            print(f"Resultado: {resultado}")
    else:
        print("Opción inválida")