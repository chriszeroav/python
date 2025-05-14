import os

os.system("clear")

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("Ejercicio1")
print("----------")

num1 = int(input("Ingresa un numero: \n"))
num2 = int(input("Ingresa otro numero: \n"))

if num1 == num2:
    print("Son iguales")
elif num1 > num2:
    print(f"El numero {num1} es mayor")
else:
    print(f"El numero {num2} es mayor")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("\nEjercicio2")
print("----------")

num1 = int(input("Ingresa un numero: \n"))
num2 = int(input("Ingresa otro numero: \n"))

operator = input("Ingresa un operador [+, -, *, /]: \n")

if operator == "+":
    print(f"La suma es { num1 + num2}")
elif operator == "-":
    print(f"La resta es { num1 - num2}")
elif operator == "*":
    print(f"La multiplicacion es { num1 * num2}")
elif operator == "/":
    print(f"La division es { num1 / num2}")
else:
    print("Operador incorrecto")


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\nEjercicio3")
print("----------")

year = int(input("Ingresa un año: \n"))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or year % 400

print("Es un año bisiesto" if isLeapYear else "No es un año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\nEjercicio4")
print("----------")

age = int(input("Ingresa tu edad: \n"))

if age >= 65:
    print("Adulto mayor")
elif age >= 18:
    print("Adulto")
elif age >= 13:
    print("Adolescente")
elif age >= 3:
    print("Niño")
else:
    print("Bebe")
