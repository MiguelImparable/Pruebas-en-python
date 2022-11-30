import os
import string

# Un programa sobre listas importadas de Strings


def Import_string():
    os.system("cls")
    print("\nExercise with Import string")

    print(string.ascii_letters)
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

    print(string.ascii_uppercase)
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ

    print(string.ascii_lowercase)
    # abcdefghijklmnopqrstuvwxyz

    print(string.digits)
    # 0123456789

    print(string.hexdigits)
    # 0123456789abcdefABCDEF

    print(string.octdigits)
    # 01234567

    print(string.printable)
    # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~♂♀

    print(string.punctuation)
    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    print(string.whitespace)
    # ♂♀

    print("\nEnd of program\n")


if __name__ == "__main__":
    Import_string()
