from mathjam.utils import *
from sympy import *

master = Tk()

deg = randint(0, 9)
func = genFunc(deg)

poly = func.replace("**", "^").replace("*", "")
print(f"Function: {poly}")
displayLatex(master, poly)

x = Symbol("x")
ans = str(integrate(func, x))
ans = ans.replace("**", "^").replace("*", "")
print(f"Answer: {ans} + C")
displayLatex(master, f"{ans} + C")

master.mainloop()
