import os

# Un programa que cree una lista de 10 num, la copie y la invierta para mostrar ambas en pantalla.


def Exercise_10():
    os.system("cls")
    print("\nExercise No.10")

    list1 = []
    list2 = []

    for i in range(10):   # Crear los valores de la lista
        list1.append(i)

    # Sorted sirve para organizar listas de manera ascendente
    list1 = sorted(list2)
    list2 = list1[::-1]   # Dejar la lista invertida

    print(f"List 1: {list1} \nList 2: {list2}")
    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_10()
