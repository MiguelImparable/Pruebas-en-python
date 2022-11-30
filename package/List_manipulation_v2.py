import os
import numpy as np

# Un programa que pida una cantidad de valores, los cuales seran añadidos a una lista, 
# seran revultos al azar y valorados asi:
# Que sean numeros menores a 100 y que sean pares, para ser añadidos a otra lista.

def List_manipulation_v2():
    os.system("cls")
    print("\nExercise for list manipulation")

    num = int(input("How many values do you want to collect?: "))
    list1 = [i for i in range(num)]
    np.random.shuffle(list1) # Revolver al azar
    list2 = [i for i in list1 if i < 100 and i % 2 == 0]

    print(f"The selected numbers were: {list2}")
    print("\nEnd of program\n")


if __name__ == "__main__":
    List_manipulation_v2()
