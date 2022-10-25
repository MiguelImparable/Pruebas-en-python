import os

# Un programa para una empresa de su sistema vacacional con las siguientes caracteristicas:
# 3 departamentos: Atencion al cliente (clave1),Logistica (clave2),Gerencia (clave3)
# (clave1): 1 año serv,  6 dias de V./ 2-6 años serv, 14 dias de V./ 7 años en adelante, 20 dias de V.
# (clave2): 1 año serv,  7 dias de V./ 2-6 años serv, 15 dias de V./ 7 años en adelante, 22 dias de V.
# (clave3): 1 año serv, 10 dias de V./ 2-6 años serv, 20 dias de V./ 7 años en adelante, 30 dias de V.


def Exercise_2():
    os.system("cls")
    print("\nExercise No.2")

    name = input("Enter the employee's name: ")
    key = int(input("Enter your password: "))
    ant = float(input("How many years have you been in the company?: "))
    day = 0

    def days_vacations(name, day):
        print(f"Employee {name} is entitled to {day} vacation days")

    if key == 1:
        if ant <= 1:
            day = 6
            days_vacations(name, day)
        elif ant >= 2 and ant <= 6:
            day = 14
            days_vacations(name, day)
        elif ant >= 7:
            day = 20
            days_vacations(name, day)

    elif key == 2:
        if ant <= 1:
            day = 7
            days_vacations(name, day)
        elif ant >= 2 and ant <= 6:
            day = 15
            days_vacations(name, day)
        elif ant >= 7:
            day = 22
            days_vacations(name, day)

    elif key == 3:
        if ant <= 1:
            day = 10
            days_vacations(name, day)
        elif ant >= 2 and ant <= 6:
            day = 20
            days_vacations(name, day)
        elif ant >= 7:
            day = 30
            days_vacations(name, day)

    else:
        print("The key does not exist")

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_2()