import os
import random

# Un programa sobre peleas pokemon


def Exercise_17():
    os.system("cls")
    print("\nExercise No.17")

    VIDA_INICIAL_PIKACHU = 80
    VIDA_INICIAL_SQUIRTTLE = 90

    vida_pikachu = VIDA_INICIAL_PIKACHU
    vida_squirttle = VIDA_INICIAL_SQUIRTTLE

    while vida_pikachu > 0 and vida_squirttle > 0:

        barra_pikachu = "|" * \
            int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
        barra_pikachu += " " * \
            int(100-(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU))

        barra_squirttle = "|" * \
            int(vida_squirttle * 100 / VIDA_INICIAL_SQUIRTTLE)
        barra_squirttle += " " * \
            int(100-(vida_squirttle * 100 / VIDA_INICIAL_SQUIRTTLE))

        print(f"\nLP Pikachu:   [{barra_pikachu}] {vida_pikachu}")
        print(f"LP Squirttle: [{barra_squirttle}] {vida_squirttle}")

        print("\nturno de pikachu")
        ataque_pikachu = random.randint(1, 2)

        if ataque_pikachu == 1:
            print("pikachu ataca con bola voltio")
            vida_squirttle -= 10
        else:
            print("pikachu ataca con onda trueno")
            vida_squirttle -= 11

        print("\nturno de Squirttle")
        ataque_squirttle = None

        while ataque_squirttle != "p" and ataque_squirttle != "a" and ataque_squirttle != "b":
            ataque_squirttle = input(
                "¿Que ataque deseas realizar?: [P] Placaje, [A] Pistola Agua, [B] Burbuja: ")

            if ataque_squirttle == "p":
                print("Squirttle Ataca con Placaje")
                vida_pikachu -= 10
            elif ataque_squirttle == "a":
                print("Squirttle Ataca con Pistola Agua")
                vida_pikachu -= 12
            elif ataque_squirttle == "b":
                print("Squirttle Ataca con Burbuja")
                vida_pikachu -= 9

        enter = input("\nPresiona ENTER para continuar: ")
        os.system("cls")

    if vida_pikachu > vida_squirttle:
        print("\nPikachu Gana")
    else:
        print("\nSquirttle Gana")

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_17()
