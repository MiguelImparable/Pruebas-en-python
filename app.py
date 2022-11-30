from package.Example_password import Example_password
from package.For_loop_v1 import For_loop_v1
import os


def main():
    os.system("cls")
    print("\nVery good, welcome to the main class")

    while input('Do you want to perform any exercise? (Y/N)= ').lower() != 'n':
        count = int(input('What exercise do you want to perform = '))
        Excercices = {
            1: Example_password,
            2: For_loop_v1
        }
        funcion = Excercices[count]
        if callable(funcion):
            funcion()
    else:
        print("\nEnd of program\n")


if __name__ == "__main__":
    main()
