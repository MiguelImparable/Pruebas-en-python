import os

# Un programa sobre lo que me saque en ingles en el ciclo 2 MIN TIC


def Exercise_22():
    os.system("cls")
    print("\nExercise No.27")

    valores = [3, 4, 6, 6, 6, 6]
    notas = [5, 5, 4.17, 2.50, 5, 4.17]
    nota_definitiva = []

    for i in range(len(valores)):
        nota = valores[i]*notas[i]
        nota_definitiva.append(nota)

    nota_definitiva = sum(nota_definitiva)/sum(valores)

    print(nota_definitiva)


if __name__ == "__main__":
    Exercise_22()
