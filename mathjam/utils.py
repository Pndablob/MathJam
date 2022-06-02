from random import *
import matplotlib as mp
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def displayLatex(master, equation):
    mp.use('TkAgg')
    master.geometry("1600x900")
    equation = "$" + equation + "$"

    label = Label(master)
    label.pack()

    fig = mp.figure.Figure(figsize=(10, 8), dpi=100)
    fig.clear()
    ax = fig.add_subplot(111)

    ax.clear()
    ax.text(0.05, 0.2, equation, fontsize=16)

    canvas = FigureCanvasTkAgg(fig, master=label)
    canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
    canvas._tkcanvas.pack(side="top", fill="both", expand=True)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    canvas.draw()


# generate a random polynomial
def genFunc(deg):
    f = ""
    for i in range(deg, 0, -1):
        coef = randint(1, 10)  # editable values
        if coef > 1:
            f += f"{coef}*"
        f += "x"
        if i > 1:
            f += f"^{i}"
        sign = randint(0, 1)  # editable values
        if sign == 1:
            f += " + "
        elif sign == 0:
            f += " - "
    c = randint(1, 50)  # editable values
    f += str(c)

    return f


def latexToMath(latex):
    return latex.replace("x", "*x").replace("^", "**")


def mathToLatex(math):
    return math.replace("**", "^").replace("*", "")


def main():
    pass


if __name__ == '__main__':
    main()

