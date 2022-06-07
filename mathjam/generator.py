from random import *
from sympy import *


# generate a random polynomial of given degree
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


#  generate random degree polynomial
def genRandDegPoly():
    d = randint(1, 8)  # editable value
    return genPoly(d)

