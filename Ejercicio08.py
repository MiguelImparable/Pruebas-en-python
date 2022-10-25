import os

# Un programa que imprima el numero mayor de una cantidad de numeros asignada por el usuario.


def Exercise_8():
    os.system("cls")
    print("\nExercise No.8")

    mayor = None
    n = int(input("How many numbers do you want to compare?: "))

    for i in range(n):
        n = float(input("Tell me a number:"))
        if mayor is None or n > mayor:
            mayor = n

    print(f"The largest number is {mayor}")
    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_8()
