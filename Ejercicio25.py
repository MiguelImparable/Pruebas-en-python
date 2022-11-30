import random
import numpy as np


def Exercise_25():
    while True:
        try:
            Calles = int(input("Introduce el numero de calles: "))
            Carreras = int(input("Introduce el numero de carreras: "))
            Habitantes = int(input("Introduce el numero de Habitantes: "))
            nvechiculos = int(input("Introduce el numero de Vehiculos: "))
        except ValueError:
            print("Copiaste una letra, vuelve a intentarlo")
            return Exercise_25()

        else:
            x1 = list(range(Calles))
            np.random.shuffle(x1)
            x2 = list(range(Carreras))
            np.random.shuffle(x2)
            MalladoVial = []
            MalladoVial2 = []
            Propietarios = []
            ListaPropietarios = []
            Vehiculos = []
            ListaSemaforos = []
            CallesList = []
            CarrerasList = []
            VehiculosList = []
            LL = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
            LV = ['a', 'e', 'i', 'o', 'u']
            NO = list(range(10))
            Puestos = ["Dos Puestos", "Cuatro Puestos", "Seis Puestos"]
            TipoVehiculo = ["Familiar", "Deportivo"]
            Lista = ["Calle", "Carrera"]
            EstSem = ["Amrillo", "Rojo", "Verde",
                      "Intermitente", "Fuera de Servicio"]
            # Calles
            for i in range(Calles):
                MalladoVial.append(x1[i])
            for i in range(Calles):
                if MalladoVial[i] % 2 == 0:
                    CallesList.append(
                        "Calle: {} Oriente".format(MalladoVial[i]))
                else:
                    CallesList.append(
                        "Calle: {} Occidente".format(MalladoVial[i]))
            # Carreras
            for i in range(Carreras):
                MalladoVial2.append(x2[i])
            for i in range(Carreras):
                if MalladoVial2[i] % 2 == 0:
                    CarrerasList.append(
                        "Carrera: {} Norte".format(MalladoVial2[i]))
                else:
                    CarrerasList.append(
                        "Carrera: {} Sur".format(MalladoVial2[i]))
            # Nombres y Apellidos Propietarios del Auto
            for i in range(Habitantes):
                np.random.shuffle(LL)
                np.random.shuffle(LV)
                c1 = "{}{}{}{}{}{}".format(
                    LL[0], LV[0], LL[1], LV[1], LL[2], LV[2])
                np.random.shuffle(LL)
                np.random.shuffle(LV)
                c1 += " {}{}{}{}{}{}".format(LL[0],
                                             LV[0], LL[1], LV[1], LL[2], LV[2])
                c1 = c1.capitalize()
                Propietarios.append(c1)

            Limite = Habitantes * 20 / 100
            Limite = int(Limite)
            ListaPropietarios = Propietarios
            for i in range(len(Vehiculos)):
                if i < Limite:
                    b1 = (Propietarios[i], Vehiculos[i], Puestos[random.randint(
                        0, 2)], TipoVehiculo[random.randint(0, 1)])
                    VehiculosList.append(b1)
            # Vehiculos
            for i in range(nvechiculos):
                np.random.shuffle(LL)
                np.random.shuffle(NO)
                c1 = LL[0] + LL[1] + LL[2] + \
                    str(NO[0]) + str(NO[1]) + str(NO[2])
                c1 = c1.capitalize()
                Vehiculos.append(c1)
            # Semaforos
            a = CallesList + CarrerasList
            np.random.shuffle(a)
            for i in range(Calles):
                x = "Semaforo: {} Estado: {}".format(
                    a[i], EstSem[random.randint(0, 4)])
                ListaSemaforos.append(x)
            # Imprimir Placas
            print("PLACAS:_______________________ \n")
            for i in range(len(Vehiculos)):
                print(f"{Vehiculos[i]}\n")
            # Imprimir Calles
            print("CALLES:_______________________ \n")
            for i in range(Calles):
                print(f"{CallesList[i]}\n")
            # Imprimir Carreras
            print("CARRERAS:_______________________ \n")
            for i in range(Carreras):
                print(f"{CarrerasList[i]}\n")
            # Imprimir Propietarios y Habitantes
            print("PROPIETARIOS:_______________________ \n")
            for i in range(len(ListaPropietarios)):
                print(f"{ListaPropietarios[i]}\n")
            # Imprimir Semaforos
            print("SEMAFOROS:_______________________ \n")
            for i in range(len(ListaSemaforos)):
                print(ListaSemaforos[i])
            print()
            break


if __name__ == "__main__":
    Exercise_25()

"""MEJORAR LOS RANDOM, REALIZAR EL PROCESO CON POO, ALISTAR CON BASE DE DATOS MYSQL, INTERFASE GRAFICA"""
