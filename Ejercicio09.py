import os

# Un programa que asigne un numero a 3 jugadores y que el programa no cierre hasta que los 3 tengan un numero asignado.


def Exercise_9():
    os.system("cls")
    print("\nExercise No.9")

    j1 = None
    j2 = None
    j3 = None

    while j1 is None or j2 is None or j3 is None:
        print(
            "\nPress [1] for Player A \nPress [2] for Player B \nPress [3] for Player C\n")
        j = int(input("choose a player: "))

        if j == 1 and j1 is None:
            j1 = int(input("tell me a number: "))
        elif j == 1 and j1 is not None:
            print("Player A has already chosen")

        elif j == 2 and j2 is None:
            j2 = int(input("tell me a number: "))
        elif j == 2 and j2 is not None:
            print("Player B has already chosen")

        elif j == 3 and j3 is None:
            j3 = int(input("tell me a number: "))
        elif j == 3 and j3 is not None:
            print("Player C has already chosen")

        else:
            print("You have entered an incorrect option")

    print(f"\nThe 3 players have already chosen number:")
    print(f"\nPlayer A: {j1} \nPlayer B: {j2} \nPlayer C: {j3}")
    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_9()
