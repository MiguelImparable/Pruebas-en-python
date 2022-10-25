import os
import numpy as np

# Un programa que pida una cantidad de valores, los cuales seran añadidos a una lista, seran revultos al azar y valorados asi:
# Que sean numeros menores a 100 y que sean pares, para ser añadidos a otra lista y mostrados en pantalla.


def Exercise_12():
    os.system("cls")
    print("\nExercise No.12")

    num = int(input("How many values do you want to collect?: "))
    list1 = []
    list2 = []

    for i in range(num):
        list1.append(i)

    np.random.shuffle(list1)

    for i in list1:
        if i < 100 and i % 2 == 0:
            list2.append(i)

    print(f"The selected numbers were: {list2}")
    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_12()
