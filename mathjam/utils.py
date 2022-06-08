import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import *


# resets canvas to a blank canvas
def updateCanvas(col, row, master, equation=None):
    mp.use('TkAgg')

    qFigure = mp.figure.Figure(figsize=(18, 3), dpi=100, tight_layout=True)
    qAxis = qFigure.add_subplot(111)
    qAxis.get_xaxis().set_visible(False)
    qAxis.get_yaxis().set_visible(False)

    if equation is not None:
        equation = mathToLatex(equation)
        qAxis.text(0.05, 0.2, equation, fontsize=16)

    qCanvas = FigureCanvasTkAgg(qFigure, master=master)
    qCanvas.get_tk_widget().grid(column=col, row=row)
    qCanvas.draw()


def getDerivative(func):
    x = Symbol('x')
    return mathToLatex(str(diff(func, x)))


def getIndefIntegral(func):
    x = Symbol('x')
    return mathToLatex(str(integrate(func, x))+" + C")


def getDefIntegral(func, a, b):
    x = Symbol('x')
    return mathToLatex(str(integrate(func, (x, a, b))))


def latexToMath(latex):
    return latex.replace("x", "*x").replace("^", "**")


def mathToLatex(math):
    return math.replace("**", "^").replace("*x", "x")

