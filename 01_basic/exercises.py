###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system

if system("clear") != 0:
    system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
name = input("Escribe tu nombre:\n")
age = int(input("Escribe tu edad:\n"))

print(f"Hola, te llamas {name} y tienes {age} años")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"Tipo de dato de {a} es {type(a)}")
print(f"Tipo de dato de {b} es {type(b)}")
print(f"Tipo de dato de {c} es {type(c)}")
print(f"Tipo de dato de {d} es {type(d)}")
print(f"Tipo de dato de {e} es {type(e)}")


print("--------------")

print("\nEjercicio 3: Casting de tipos")
print('Convierte la cadena "12345" a un entero y luego a un float.')
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
dato1 = "12345"
dato1_int = int(dato1)
dato1_float = float(dato1_int)

print(f"El tipo de dato final es: {type(dato1_float)}")

dato2 = 3.99
dato2_int = int(dato2)
print(f"El {dato2} convertido a entero es {dato2_int}")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
my_name = "Christopher"
my_age = 21
my_height = 1.70

print(f"Hola! Me llamo {my_name} y tengo {my_age} años, mido {my_height} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

PI = 3.1416
PI_ROUND = round(PI)
result = int(PI_ROUND / 2)
print(f"El resultado es: {result}")
