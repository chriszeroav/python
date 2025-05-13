###
# 05 - Entrada (input())
# EL usuario va a poder ingresar informacion en la consola
###

name = input("Hola, ¿Cómo te llamas?\n")

print(f"Encantado de conocerte, {name}")


age = input("¿Cuantos años tienes?\n")
print(f"Dentro de 10 años tendras, {int(age) + 10}")

print("Obtener multiples vaslores")
country, city = input("¿En que país y ciudad vives?\n").split()


print(f"Vives en {country}, {city}")
