from sympy import *
from random import *
from tkinter import *
import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def displayLatex(master, equation):
    mp.use('TkAgg')
    master.geometry("1600x900")
    equation = "$" + equation + "$"

    label = Label(master)
    label.pack()

    fig = mp.figure.Figure(figsize=(10, 4), dpi=100)
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
def genPoly(deg):
    if randint(0, 1) == 0:
        p = ""
    else:
        p = "-"
    for i in range(deg, 0, -1):
        coef = randint(1, 10)  # editable values
        if coef > 1:
            p += f"{coef}*"

        p += "x"

        if i > 1:
            p += f"^{i}"

        sign = randint(0, 1)  # editable values
        if sign == 1:
            p += " + "
        elif sign == 0:
            p += " - "

    c = randint(1, 50)  # editable values
    p += str(c)

    return p


def genIntEquation(func, a=None, b=None):
    return "\\int{a}{b} " + func + "\\, dx"


def getRandDegPoly():
    d = randint(1, 8)  # editable value
    return genPoly(d)


def getIntegral(func):
    x = Symbol('x')
    return mathToLatex(str(integrate(func, x)))


def getDerivative(func):
    x = Symbol('x')
    return mathToLatex(str(diff(func, x)))


def latexToMath(latex):
    return latex.replace("x", "*x").replace("^", "**")


def mathToLatex(math):
    return math.replace("**", "^").replace("*x", "x")


def main():
    pass


if __name__ == '__main__':
    main()
