# Un programa sobre una lista de compra
import os


def Example_shopping_list():
    os.system("cls")
    print("\nExample shopping list")

    SALIDA = "salir"
    lista_predefinida = ["mango", "banano", "platano", "leche", "limon"]

    def preguntar_producto():
        return (input(f"\nIntroduce un producto [({SALIDA}) para salir]: "))

    def archivo(lista_compra):
        nombre_archivo = "lista de la compra"
        # w de write, r de read, a de append
        with open(f"{nombre_archivo}.txt", "w") as mi_archivo:
            mi_archivo.write("\n".join(lista_compra))

    def lista_de_compra():
        lista_compra = []
        input_usuario = None

        if input("Quieres cargar la ultima lista de la compra?: [Y/N]: ") == "S":
            with open("lista de la compra", "r") as a:
                lista_compra = a.read()

        while input_usuario != SALIDA:
            input_usuario = preguntar_producto().lower()  # convertir a minuscula el input

            if input_usuario in lista_predefinida:

                if input_usuario in lista_compra:
                    print("El producto ya esta en la lista")

                else:
                    lista_compra.append(input_usuario)
                    print("\n".join(lista_compra))

            elif input_usuario not in lista_predefinida and input_usuario != SALIDA:
                print("\nEl producto no puede ser incluido por no estar en las opciones")
                print("Opciones: ")
                print(", ".join(lista_predefinida))

        archivo(lista_compra)
        print("\nEnd of program\n")

    lista_de_compra()


if __name__ == "__main__":
    Example_shopping_list()
