import os
import random

# Un programa en el cual el usuario debera adivinar un numero de 1 a 10 para que adivine.
# Felicitarlo si adivina o si no terminar el juego.


def Exercise_14():
    os.system("cls")
    print("\nExercise No.14")
    print("Guess a number from 1 to 10")

    num = int(input("What number do you think it is?: "))
    num2 = random.randint(1, 10)

    if num == num2:
        print("YOU WIN... you guessed the number")

    else:
        print(f"YOU LOSE... You did not guess, the number was the {num2}")

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_14()
