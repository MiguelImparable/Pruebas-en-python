# Un programa que me permita practicas en PDS y los DF
import os
import pandas as pd


def Import_pandas():
    os.system("cls")
    print("\nExercise for Import pandas")
    # Archivos mas comunes DataFrame o formato tabla:
    # 1. CSV - Comma Separated Values
    # 2. TSV - Tab Separated Values
    # 3. XLSX - Excel
    # Pandas series, son arrays np que son cada una de las columnas con su propio indice y titulo

    # Creando un DataFrame desde cero (diccionario)
    datos = {"nombre": ["SFDX Show", "Sara Nogark", "Nate Gentile", "Bettatech", "Antonio Sarosi", "Edgar Pons", "S4vitar"],
             "especialidad": ["Hardware", "Edición de video", "Programación", "Programación", "Sistemas operativos", "Robotica", "Hacking"],
             "edad": [28, 31, 30, 29, 31, 30, 28],
             "visitas": [102977, 134031, 121325, 116988, 128723, 105642, 102764],
             }
    df = pd.DataFrame(datos)

    # Crear columna
    df["sexo"] = ["H", "M", "H", "H", "H", "H", "H"]

    # Explorar un DataFrame
    df.head()  # vacio muestra las primeras 5 filas del DataFrame
    df.head(2)  # Muestra la cantidad asignada
    df.tail()  # vacio muestra las ultimas 5 filas del DataFrame
    df.tail(2)  # Muestra la cantidad asignada
    df.sample()  # vacia nos da una fila aleatoria
    df.sample(2)  # con valor muestra la fila asignada
    df.info()  # informacion del DataFrame
    df.describe()  # info valores numericos estadisticos
    # Se puede especificar el valor estadistico a adquirir
    df.describe()["edad"]["max"]
    df.shape  # que forma tiene
    df.columns  # devuelve una lista con las columnas de nuestro DF
    df.index  # lista con los indices, en general, un rango de valores num

    # Acceso mediante etiquetas
    df["especialidad"][2]  # retorna el DF especialidad en la posicion 2
    df["nombre"] == "Nate Gentile"  # retorna valores vooleanos
    # retorna las columnas donde la condicion sea true
    df[df["nombre"] == "Nate Gentile"]
    # retorna solo la condicion
    df[df["nombre"] == "Nate Gentile"]["especialidad"]

    # Buscar elementos integer location
    # no. fila, no. columna (los dos puntos generan rangos en ambas posiciones)
    df.iloc[2, 0:2]

    # Bucar elementos location
    df.loc[2, "especialidad":"visitas"]
    # rangos vacios son valores iniciales o finales depende del uso
    df.loc[2, "especialidad":]

    print("\nEnd of program\n")


if __name__ == "__main__":
    Import_pandas()
