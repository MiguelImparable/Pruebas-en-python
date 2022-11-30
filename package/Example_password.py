# Un programa que asigne una contraseña con ciertas caracteristicas:
# Que tengas mayus, minus, caracteres especiales, numeros con maximo 3 intentos.
import os
import string


def Example_password():
    os.system("cls")
    print("\nExercise for Example password")

    mayus = string.ascii_uppercase  # Mayus List
    minus = string.ascii_lowercase  # Minus List
    num = string.octdigits  # Numbers
    esp = string.punctuation  # Specials Cases
    password = None
    picking_out = True
    Attempts = 0

    while picking_out:
        Attempts += 1
        password_attempts = input("Choose your password: ")

        long = False
        may = False
        min = False
        n = False
        es = False

        if len(password_attempts) >= 8 and len(password_attempts) <= 15:
            long = True
            for caracter in password_attempts:
                if caracter in mayus:
                    may = True
                if caracter in minus:
                    min = True
                if caracter in num:
                    n = True
                if caracter in esp:
                    es = True

        if long and may and min and n and es:
            print("The password has been chosen correctly")
            password = password_attempts
            picking_out = False

        else:
            if not long:
                print("The password must be between 8 and 15 characters")
            elif not may:
                print("The password must have at least one capital letter")
            elif not min:
                print("The password must have at least one lowercase")
            elif not n:
                print("The password must have at least one number")
            elif not es:
                print("Password must have at least one Special Character")

        if Attempts > 3:
            picking_out = False

    if password:
        print(f"your password is: {password}")

    else:
        print("Failed to set password")

    print("\nEnd of program\n")


if __name__ == "__main__":
    Example_password()
