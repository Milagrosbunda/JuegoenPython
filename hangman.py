import random
print("Bienvenido al juego.")
print("Ingrese un color: ")

colores = ("rojo", "azul", "verde", "amarillo",
           "purpura", "lila", "naranja", "celeste", "rosa",
           "fucsia", "violeta", "blanco", "negro", "gris",
           "dorado", "plateado", "turquesa")

palabra = random.choice(colores)

intentos = 7
while intentos > 0:
    guess = input()
    if guess != palabra:
        print("Mal!")
        intentos -= 1
        if intentos == 6:
            print("________")
            print("|       O")
            print("|")
            print("|_")
        if intentos == 5:
            print("________")
            print("|       O")
            print("|       |")
            print("|_")

        if intentos == 4:
            print("________")
            print("|       O")
            print("|       |")
            print("|_")
        if intentos == 3:
            print("________")
            print("|       O")
            print("|      -|")
            print("|_")
        if intentos == 2:
            print("________")
            print("|       O")
            print("|      -|-")
            print("|_")
        if intentos == 1:
            print("________")
            print("|       O")
            print("|      -|-")
            print("|_       \ ")

        print("Intenta de nuevo: ")

    if guess == palabra:
        break

if guess == palabra:
    print("Ganaste!")
if guess != palabra:
    print("_______")
    print("|      0")
    print("|     -|-")
    print("|_    / \ ")

    print("Te has quedado son intentos, la palabra era: " + palabra)
