import os

# Un programa que entre 3 numeros seleccione el mas grande.


def Exercise_4():
    os.system("cls")
    print("\nExercise No.4")

    def largest_number():
        list_nums = []

        for n in range(3):
            num = float(input("Enter No: "))
            list_nums.append(num)

        print(f" the largest number is: {max(list_nums)}")

    largest_number()
    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_4()
