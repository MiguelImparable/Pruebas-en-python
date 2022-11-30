# Un programa que cree una lista de 10 num, la copie y la invierta para mostrar ambas en pantalla.
import os
import random


def List_manipulation_v1():
    os.system("cls")
    print("\nExercise for list manipulation")

    list1 = sorted([random.randint(1, 100) for n in range(10)])
    list2 = list1[::-1]   # Dejar la lista invertida

    print(f"List 1: {list1} \nList 2: {list2}")
    print("\nEnd of program\n")


if __name__ == "__main__":
    List_manipulation_v1()
