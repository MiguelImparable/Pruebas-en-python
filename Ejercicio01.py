import os

# Un programa que muestre mi nombre, cedula y correo en pantalla.


def Exercise_1():
    os.system("cls")
    print("\nExercise No.1")

    def greeting(name, cc, mail):
        print(f"My name is {name}, with ID No.{cc} and my email is {mail}\n")

    greeting("Miguel Angel Diaz Delgado", 1214743715, "migerodd888@gmail.com")
    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_1()
