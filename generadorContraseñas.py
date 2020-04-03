

import random

minusculas = "qwertyuiopasdfghjklzxcvbnm"
mayusculas = minusculas.upper()
numeros = ("1234567890")
simbolos = ("+-_/%&$#¡!")

todo_posible = minusculas + mayusculas+numeros+simbolos

print("Vamos a generar una contraseña.")
minimo = int(input("Elige un minimo de caracteres: "))
maximo = int(input("Elige un maximo de caracteres: "))
largo = random.choice(range(minimo, maximo))

contraseña = "".join(random.sample(todo_posible, largo))
print(contraseña)
