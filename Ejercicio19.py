import os

# Un programa sobre listas y su uso avanzado


def Exercise_19():
    os.system("cls")
    print("\nExercise No.19")

    numeros_usuario = []
    numero_introducido = int(input("introduzca un número en la lista: "))
    numeros_usuario.append(numero_introducido)

    # INPUT dentro del while
    while input("¿Desea introducir más números? [S/N]: ") == "S":
        numero_introducido = int(input("introduzca un número en la lista: "))
        numeros_usuario.append(numero_introducido)

    print(numeros_usuario)

    # Comprension de lista
    numeros_usuario = [str(numero) for numero in numeros_usuario]
    print(numeros_usuario)
    print(type(numeros_usuario))

    lista = numeros_usuario
    max = lista[0]

    for x in lista:
        if x > max:
            max = x

    min = lista[0]
    for x in lista:
        if x < min:
            min = x

    print(min, max)
    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_19()
