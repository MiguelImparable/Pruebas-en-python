# Un programa que separe los numeros de pares o impares, la cantidad asignada por el usuario (par es 0, impar es 1).
import os


def While_loop():
    os.system("cls")
    print("\nExercise with while loop")

    no = int(input("Enter the integer value you want to separate: "))
    peers = []
    odds = []
    x = 0

    while x < no:
        if x % 2 == 0:
            peers.append(x)
        elif x % 2 != 0:
            odds.append(x)
        x += 1

    print(f"Pares: {peers} \nImpares: {odds}")
    print("\nEnd of program\n")


While_loop()
