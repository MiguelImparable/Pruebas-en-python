import os

# Un programa que haga un milo.


def Exercise_13():
    os.system("cls")
    print("\nExercise No.13")
    print("we are going to prepare a very powerful milo")

    kitchen = input("Let's go to the kitchen? (Y/N): ")

    if kitchen == "Y":
        milk = input("Is there milk in the fridge? (Y/N): ")

        if milk == "Y":
            milo = input("Is there milo in the pantry? (Y/N): ")

            if milo == "Y":
                print("we serve the milk")
                print("\nWe stir the milo")
                print("\nWe have our milo ready")

            else:
                print("There is no milo in the pantry, it cannot be prepared")
        else:
            print("There's no milk in the fridge, we can't make the milo")
    else:
        print("We can't go to the kitchen, we have no way to prepare the milo")

    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_13()
