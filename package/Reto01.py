# Un programa que realice una Lista de compras de una tienda según especificaciones técnicas.
import os


def Exercise_RETO1():
    os.system("cls")
    print("\nExercise RETO1")

    total = 0
    product_list = []

    def product(total):
        text = "del producto"
        name = input(f"Nombre {text}: ")
        cost = float(
            input(f"Valor unitario {text}: ") * input(f"Cantidad {text}: "))
        iva = input("¿El producto cuenta con IVA? [S/N]: ").lower
        total += cost

        if iva == "s":
            print("IVA INCLUIDO")
        elif iva == "n":
            print("PRODUCTO SIN IVA")
        else:
            print("Error de datos en el programa")

        print(f"SUBTOTAL: {cost}")
        return total

    while input("¿Faltan productos por cobrar en esta compra? [S/N]: ").lower == "s":
        product(total)
    else:
        print("Error de datos en el programa")

    print(f"TOTAL A COBRAR: {total}")

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_RETO1()
