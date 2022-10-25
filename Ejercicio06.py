import os

# Un programa que imprima en pantalla la sucesion de fibonacci preguntando el valor maximo al usuario.


def Exercise_6():
    os.system("cls")
    print("\nExercise No.6")

    def fibonacci(n):
        a = 0
        b = 1
        fib = []

        if a < n:
            fib.append(a)
        if b < n:
            fib.append(b)

        for k in range(n):
            c = a + b
            a = b
            b = c

            if b < n:
                fib.append(b)

        return print(fib)

    if __name__ == "__main__":
        fibonacci(int(input("up to what value do you want to indent: ")))

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_6()
