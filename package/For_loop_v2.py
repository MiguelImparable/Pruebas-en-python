import os

# Un programa sobre lo que me saque en ingles en el ciclo 2 MIN TIC


def For_loop_v2():
    os.system("cls")
    print("\nExercise No.27")

    valores = [3, 4, 6, 6, 6, 6]
    notas = [5, 5, 4.17, 2.50, 5, 4.17]
    nota_definitiva = sum([valores[i]*notas[i] for i in range(len(valores))])/sum(valores)

    print(nota_definitiva)


if __name__ == "__main__":
    For_loop_v2()
