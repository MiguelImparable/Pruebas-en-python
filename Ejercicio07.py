import os

# Un programa que almacene las asignaturas de un curso en una lista, asigne sus calificaciones y los muestre en pantalla.


def Exercise_7():
    os.system("cls")
    print("\nExercise No.7")

    subject = []
    note = []
    grades = []

    n = int(input("How many Subjects do you want to add to the list?: "))
    m = 0

    while m < n:
        m += 1
        subject = input("Name of the subject: ")
        note = float(input("subject note: "))
        grades.append(subject)
        grades.append(note)

    m = 0
    print("")

    while m < len(grades):
        print(f"In the subject: {grades[m]} your grade is: {grades[(m+1)]}")
        m += 2

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_7()
