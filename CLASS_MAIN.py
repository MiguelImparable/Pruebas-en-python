from Ejercicio01 import Exercise_1
from Ejercicio02 import Exercise_2
from Ejercicio03 import Exercise_3
from Ejercicio04 import Exercise_4
from Ejercicio05 import Exercise_5
from Ejercicio06 import Exercise_6
from Ejercicio07 import Exercise_7
from Ejercicio08 import Exercise_8
from Ejercicio09 import Exercise_9
from Ejercicio10 import Exercise_10
from Ejercicio11 import Exercise_11
from Ejercicio12 import Exercise_12
from Ejercicio13 import Exercise_13
from Ejercicio14 import Exercise_14
from Ejercicio15 import Exercise_15
from Ejercicio16 import Exercise_16
from Ejercicio17 import Exercise_17
from Ejercicio18 import Exercise_18
from Ejercicio19 import Exercise_19
from Ejercicio20 import Exercise_20
from Ejercicio21 import Exercise_21
from Ejercicio22 import Exercise_22
from Ejercicio23 import Exercise_23
from Ejercicio24 import Exercise_24

import os


def main():
    os.system("cls")
    print("\nVery good, welcome to the main class")

    while input('Do you want to perform any exercise? (Y/N)= ').lower() != 'n':
        Exc = int(input('What exercise do you want to perform = '))
        if Exc == 1:
            Exercise_1()
        if Exc == 2:
            Exercise_2()
        if Exc == 3:
            Exercise_3()
        if Exc == 4:
            Exercise_4()
        if Exc == 5:
            Exercise_5()
        if Exc == 6:
            Exercise_6()
        if Exc == 7:
            Exercise_7()
        if Exc == 8:
            Exercise_8()
        if Exc == 9:
            Exercise_9()
        if Exc == 10:
            Exercise_10()
        if Exc == 11:
            Exercise_11()
        if Exc == 12:
            Exercise_12()
        if Exc == 13:
            Exercise_13()
        if Exc == 14:
            Exercise_14()
        if Exc == 15:
            Exercise_15()
        if Exc == 16:
            Exercise_16()
        if Exc == 17:
            Exercise_17()
        if Exc == 18:
            Exercise_18()
        if Exc == 19:
            Exercise_19()
        if Exc == 20:
            Exercise_20()

    else:
        print("\nEnd of program\n")


if __name__ == "__main__":
    main()

