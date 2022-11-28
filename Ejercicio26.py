class Calculadora:
    def __init__(self, numero):  # Importante siempre generar el constructor
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresar_dato(self):
        self.datos = [int(input("ingresar datos: " + str(i+1) + "= "))
                      for i in range(self.n)]


class Operaciones_Basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)  # Limitar los atributos a 2

    def suma(self):
        a, b = self.datos
        s = a + b
        print("El resultado es: ", s)

    def resta(self):
        a, b = self.datos
        s = a-b
        print("El resultado es: ", s)

    def multiplicacion(self):
        a, b = self.datos
        s = a*b
        print("El resultado es: ", s)

    def Division(self):
        a, b = self.datos
        s = a/b
        print("El resultado es: ", s)


class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def Cuadrada(self):
        import math
        a, = self.datos
        print("El resultado es: ", math.sqrt(a))


def Exercise_26():
    Ejemplo = Operaciones_Basicas()
    print(Ejemplo.ingresar_dato())
    print(Ejemplo.resta())
    print(isinstance(Ejemplo, raiz))  # Verificar la herencia
    print(issubclass(Operaciones_Basicas, Calculadora))  # Verificar subclase


if __name__ == "__main__":
    Exercise_26()
