import os

os.system("clear")

print("Sentencia simple condicional")

age = 18

if age >= 30:
    print("Eres un adulto")
elif age >= 18:
    print("Eres un adolescente")
else:
    print("Eres un joven")

carnet = "si"

if carnet == "si":
    print("Si puedes conducir")
else:
    print("No puedes conducir")

note = 9

if note >= 9:
    print("Sobresaliente")
elif note >= 7:
    print("Notable")
elif note >= 5:
    print("Aprobado")
else:
    print("No estas calificado")


print("Condiciones Multiples")

age = 25
tiene_carnet = False

if age >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

es_fin_de_semana = False

if not es_fin_de_semana:
    print("Hay que trabajar")
else:
    print("Hoy toca descansar")


print("Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes comprar comida")
    else:
        print("No puedes comprar comida")
else:
    print("Quedate en casa")


print("\nCondicion ternaria")

age = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"

print(mensaje)
