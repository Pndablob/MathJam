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
    ax.text(0.2, 0.6, equation, fontsize=16)

    canvas = FigureCanvasTkAgg(fig, master=label)
    canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
    canvas._tkcanvas.pack(side="top", fill="both", expand=True)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    canvas.draw()


def genPoly(deg):
    p = ""
    for i in range(deg, 0, -1):
        coef = randint(0, 10)
        if coef > 1:
            p += f"{coef}"
        p += "x"
        if i > 1:
            p += f"^{i}"
        sign = randint(0, 1)
        if sign == 1 and p != "" and coef != 0:
            p += "+"
        elif sign == 0:
            p += "-"
    c = randint(1, 50)
    p += str(c)

    return p


def main():
    pass


if __name__ == '__main__':
    main()

