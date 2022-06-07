from sympy import *


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


def answerCheck(eq, ans):
    pass
