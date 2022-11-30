import os
import json
import csv

# Un programa que revise un documento y analice sus datos según especificaciones técnicas.


def Exercise_RETO5():
    os.system("cls")
    print("\nExercise RETO5")

    def solucion():
        archivo = open('TESLA.csv')
        x = csv.reader(archivo)
        Date = []
        Open = []
        High = []
        Low = []
        Close = []
        Adj_Close = []
        Volume = []

        next(x, None)
        for i in x:
            Date.append(i[0])
            Open.append(float(i[1]))
            High.append(float(i[2]))
            Low.append(float(i[3]))
            Close.append(float(i[4]))
            Adj_Close.append(float(i[5]))
            Volume.append(int(i[6]))

        archivo.close()
        n = len(Date)

        alza = []
        Abs = []
        s = []

        for i in range(n):
            resta = Close[i] - Open[i]
            Abs.append(abs(Close[i] - Adj_Close[i]))
            s.append(abs(Low[i] - High[i]))

            if resta > 0:
                alza.append('SUBE')

            elif resta < 0:
                alza.append('BAJA')

            elif resta == 0:
                alza.append('ESTABLE')

        # Creación de archivo CSV
        with open('analisis_archivo.csv', 'w') as file:
            file.write(
                'Fecha \tComportamiento de la accion \tAjuste Cuadratico de Close\n')

            for i in range(n):
                file.write('%s\t' % Date[i])
                file.write('%s\t' % alza[i])
                file.write('%s\n' % Abs[i])

                file.close()

        dic = min(Open)
        lowest = {}
        highest = max(Close)
        mean = sum(Volume)/len(Volume)
        greatest = max(s)

        for i in range(n):
            if Open[i] == lowest:
                dic['date_lowest_open'] = Date[i]
                dic['lowest_open'] = lowest

            if Close[i] == highest:
                dic['date_highest_close'] = Date[i]
                dic['highest_close'] = highest

            dic['mean_volume'] = mean

            if s[i] == greatest:
                dic['date_greatest_difference'] = Date[i]
                dic['greatest_difference'] = greatest

        with open('detalles.json', 'w') as file:
            json.dump(dic, file)

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_RETO5()
