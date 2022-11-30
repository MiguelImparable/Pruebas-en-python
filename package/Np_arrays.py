# Un programa que me permita practicas LOS NP ARRAYS
import os
import numpy as np


def Np_arrays():
    os.system("cls")
    print("\nExercise for Np arrays")

    a = np.sqrt(25)  # Raiz Cuadrada - SQuare RooT.
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    c = np.array(a)
    d = np.arange(4, 24, 2)  # No. inicial, No. final, Separación Entre Nos.
    e = np.linspace(1, 40)  # Generar en espacios iguales los numeros dados.
    f = np.zeros(8)  # cantidad x de ceros en lista
    g = np.ones(8)

    # Arreglos bidimensionales
    h = np.array([f, g])
    i = g.shape  # Datos del array (Dimensiones, Longitud de sus dimensiones)
    j = g.size  # Cuantos elementos contiene en total
    k = g.ndim  # Dimensiones

    # Operaciones con Arrays
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    array_1 = np.array(list1)
    array_2 = np.array(list2)

    l = array_1 * array_2
    # lo mismo a "l" pero con mas tiempo en ejecucion
    m = [num1*num2 for num1, num2 in zip(list1, list2)]

    # Funciones
    # Reformar (x dimensiones, valores por dimension)
    n = np.reshape(h, (4, 4))
    # x dimensiones * valores por dimension tienen que ser = a los valores del array inicial
    ñ = h.T  # Permuta los Ejes de un Array
    o = np.random.randint(0, 300)  # No. aleatorio entre los limites (x, y)
    # Condicion, Ejecución, Segunda condicion(si no es asi entonces...)
    p = np.where(h == 1, h * 10, h - 5)
    # Segunda condicion no es obligatoria

    # Un Array = media de altura 1.75mt, Desviación Est. de 5cm, con una cantidad de 1000 datos
    array_normal = np.random.normal(1.75, 0.05, 1000)
    q = np.mean(array_normal)  # Media de los datos del array
    r = np.median(array_normal)  # Mediana de los datos del array
    s = np.std(array_normal)  # Desviación Est.

    print()
    print("\nEnd of program\n")


if __name__ == "__main__":
    Np_arrays()
