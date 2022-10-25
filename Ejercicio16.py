import os

# Un programa que realice 2 preguntas


def Exercise_16():
    os.system("cls")
    print("\nExercise No.16")
    print("How much do you like cheese?\n")

    score = 0

    q1 = "Question 1: what do you do when you see a cheese board?"
    print(q1)
    print("_"*len(q1))
    print("A. I run away \nB. I try one of the cheeses, or even several \nC. I can't help devouring it")
    answers = input(": ")

    if answers == "A" or answers == "a":
        score += 10
    elif answers == "B" or answers == "b":
        score += 20
    elif answers == "C" or answers == "c":
        score += 30

    q2 = "Question 2: how would you like the hamburger?"
    print(q2)
    print("_"*len(q2))
    print("A. Without cheese \nB. With cheese \nC. I can't help devouring it")
    answers = input(": ")

    if answers == "A" or answers == "a":
        score += 10
    elif answers == "B" or answers == "b":
        score += 20
    elif answers == "C" or answers == "c":
        score += 30

    r = f"\nYour score was: {score}"

    print(r)
    print("_"*len(r))
    print("\nEnd of program\n")


if __name__ == "__main__":
    Exercise_16()
