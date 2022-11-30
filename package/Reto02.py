import os

# Un programa que filtre una lista de pacientes de una veterinaria según especificaciones técnicas.


def Exercise_RETO2():
    os.system("cls")
    print("\nExercise RETO2")

    def veterinaria(nombres, tipos, edades, pesos):

        diccionario = {}

        beneficiarios_can_fel = {}
        suma_edades_can_fel = 0
        contador_can_fel = 0
        promedio_can_fel = None
        flag1 = False
        j = 1

        beneficiarios_equ_bov = {}
        suma_edades_equ_bov = 0
        contador_equ_bov = 0
        promedio_equ_bov = None
        flag2 = False
        k = 1

        for i in range(len(nombres)):
            valor_diccionario = []
            valor_diccionario.append(nombres[i])
            valor_diccionario.append(tipos[i])
            valor_diccionario.append(edades[i])
            valor_diccionario.append(pesos[i])
            diccionario[str(i + 1)] = valor_diccionario

            if tipos[i] == "canino" or tipos[i] == "felino":
                if edades[i] >= 9:
                    valor_beneficiarios_can_fel = []
                    suma_edades_can_fel = suma_edades_can_fel+edades[i]
                    valor_beneficiarios_can_fel.append(nombres[i])
                    valor_beneficiarios_can_fel.append(tipos[i])
                    valor_beneficiarios_can_fel.append(pesos[i])

                    contador_can_fel += 1
                    flag1 = True
                    j += 1

            if tipos[i] == "equino" or tipos[i] == "bovino":
                if edades[i] >= 16:
                    valor_beneficiarios_equ_bov = []
                    suma_edades_equ_bov = suma_edades_equ_bov+edades[i]
                    valor_beneficiarios_equ_bov.append(nombres[i])
                    valor_beneficiarios_equ_bov.append(tipos[i])
                    valor_beneficiarios_equ_bov.append(pesos[i])

                    contador_equ_bov += 1
                    flag2 = True
                    k += 1

            if flag1:
                beneficiarios_can_fel[str(j - 1)] = valor_beneficiarios_can_fel
            if flag2:
                beneficiarios_equ_bov[str(k - 1)] = valor_beneficiarios_equ_bov

        if flag1:
            promedio_can_fel = suma_edades_can_fel/contador_can_fel
        if flag2:
            promedio_equ_bov = suma_edades_equ_bov/contador_equ_bov

        return diccionario, beneficiarios_can_fel, beneficiarios_equ_bov, promedio_can_fel, promedio_equ_bov

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_RETO2()
