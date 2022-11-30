# Un programa al que se le ingresen numeros y seleccione el mas grande.
import os


def For_loop_v1():
    os.system("cls")
    print("\nExercise with for loop")

    count = int(input('How many numbers do you want to compare?: '))
    list_nums = [float(input("Enter No: ")) for n in range(count)]

    print(f" the largest number is: {max(list_nums)}")
    print("\nEnd of program\n")


if __name__ == "__main__":
    For_loop_v1()
