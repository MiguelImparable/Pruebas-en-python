import os

# Un programa que ayuda a ahoorar mostrando en meses, cuanto se necesita con el valor ahorrado para alcanzar una meta.


def Exercise_5():
    os.system("cls")
    print("\nExercise No.5")

    saving = float(input("Enter the value to save: "))
    will = float(input("Enter the value to obtain with the savings: "))
    month = 1
    value = saving

    def comparison(month, saving):
        print(f"In the month {month}, you have {saving} pesos Col")

    while saving < will:
        comparison(month, saving)
        saving += value
        month += 1

    comparison(month, saving)
    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_5()
