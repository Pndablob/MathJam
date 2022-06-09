from random import *


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
def genRandDegPoly(a, b):
    d = randint(a, b)  # editable value
    return genPoly(d)


def genSimpleChain():
    p = ""
    p += str(randint(1, 50))

    if randint(0, 1) == 0:
        p += "*sin("
    else:
        p += "*cos("

    if randint(0, 1) == 0:
        p += genRandDegPoly(1, 3) + ")"
    else:
        p += f"{randint(1, 20)} + x)"

    return p
