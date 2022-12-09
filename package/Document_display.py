import matplotlib.pyplot as plt
import os


def Document_display():
    def one_line():
        os.system("cls")
        print("\nExercise for document display")

        # 1. Estructura
        x = list(range(10))
        y = x

        # 1.1 Figura
        fig = plt.figure(figsize=(10, 6))

        # 1.2 Axes
        plt.title('ONE LINE')
        plt.plot(x, y)
        plt.show()

    def generate_bar_chart(labels, values):
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        plt.show()


if __name__ == "__main__":
    Document_display()
