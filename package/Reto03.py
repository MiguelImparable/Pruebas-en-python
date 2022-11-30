import os
import numpy as np

# Un programa que realice un juego de casino según especificaciones técnicas.


def Exercise_RETO3():
    os.system("cls")
    print("\nExercise RETO3")

    def balotera(balotas):
        np.random.shuffle(balotas)
        diccionario = {"i": 0, "B": 0, "I": 0, "N": 0, "G": 0, "O": 0}

        for balota in balotas:
            if diccionario["B"] >= 5 and diccionario["I"] >= 5 and \
                    diccionario["G"] >= 5 and diccionario["O"] >= 5 and \
                    diccionario["N"] >= 4:
                break

            diccionario[balota[0]] += 1
            diccionario["i"] += 1
            print(diccionario)

        return balotas[:diccionario["i"]]

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_RETO3()
