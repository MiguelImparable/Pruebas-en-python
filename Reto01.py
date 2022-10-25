import os

# Un programa que realice una Lista de compras de una tienda según especificaciones técnicas.


def Exercise_RETO1():
    os.system("cls")
    print("\nExercise RETO1")

    w = float(input("Ingrese el valor unitario: "))
    i = input("¿El producto cuenta con IVA? [S/N]: ")
    a = float(
        input("Ingrese la cantidad que lleva el cliente del producto a registrar: "))

    if i == "S":
        w = w * a
        print("IVA INCLUIDO")
        print(f"SUBTOTAL: {w}")

    elif i == "N":
        w = w * a
        print("PRODUCTO SIN IVA")
        print(f"SUBTOTAL: {w}")

    else:
        print("Error de datos en el programa")

    b = input("¿Faltan productos por cobrar en esta compra? [S/N]: ")

    while b == "S":
        w2 = float(input("Ingrese el valor unitario: "))
        i2 = input("¿El producto cuenta con IVA? [S/N]: ")
        a2 = float(
            input("Ingrese la cantidad que lleva el cliente del producto a registrar:"))

        if i2 == "S":
            w2 = w2 * a2
            w += w2
            print("IVA INCLUIDO")
            print(f"SUBTOTAL: {w}")
            b = input("¿Faltan productos por cobrar en esta compra? [S/N]: ")

        elif i2 == "N":
            w2 = w2 * a2
            w += w2
            print("PRODUCTO SIN IVA")
            print(f"SUBTOTAL: {w}")
            b = input("¿Faltan productos por cobrar en esta compra? [S/N]: ")

    if b == "N":
        print(f"TOTAL A COBRAR: {w}")

    else:
        print("Error de datos en el programa")

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_RETO1()
