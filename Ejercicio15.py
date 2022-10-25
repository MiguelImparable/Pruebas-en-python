import os

# Un programa que aplique descuentos dependiendo de la situacion del comprador.


def Exercise_15():
    os.system("cls")
    print("\nExercise No.15")

    age = int(input("How old are you?: "))
    name = input("What`s your name?: ")
    type_of_card = ["E", "P", "F", "N"]
    flag_card = False
    flag_age = False

    print("types of card: ")
    print("\nE: student \nP: pensioner \nF: large family \nN: None")
    card = input("\nWhat type of card are you?: ")

    if card in type_of_card and card != "N":
        flag_card = True
    if 25 <= age <= 35 or age <= 10 or age >= 65:
        flag_age = True

    if flag_age or flag_card:
        print(
            f"In good time {name}, you are entitled to a 25% discount in the store")

    else:
        print("You are not entitled to any kind of discount")

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_15()
