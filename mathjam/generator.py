from mathjam.utils import *
from sympy import *


def main():
    master = Tk()

    poly = getRandDegPoly()
    func = mathToLatex(poly)
    print(f"Function: {func}")
    displayLatex(master, func)

    x = Symbol("x")
    ans = getIntegral(poly)
    print(f"Integral Answer: {ans} + C")
    displayLatex(master, f"{ans} + C")

    ans = getDerivative(poly)
    print(f"Derivative Answer: {ans}")
    displayLatex(master, ans)

    master.mainloop()


def main2():
    master = Tk()

    s = ""
    for i in range(10):
        poly = mathToLatex(getRandDegPoly())
        print(poly)
        s += poly + "\n"

    s += " "

    print(s)

    displayLatex(master, s)
    master.mainloop()


if __name__ == '__main__':
    main2()
