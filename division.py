def dividir(a, b, c):
    try:
        return a / b / c
    except ZeroDivisionError:
        return "Error: no se puede dividir entre 0"

# Ejemplo de uso
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

resultado = dividir(num1, num2, num3)
print("Resultado:", resultado)