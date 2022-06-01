from mathjam.utils import *

master = Tk()
deg = randint(0, 10)
poly = genPoly(deg)
print(poly)
displayLatex(master, poly)
master.mainloop()
