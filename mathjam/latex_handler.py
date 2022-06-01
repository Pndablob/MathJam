import matplotlib as mp
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Root:
    def __init__(self, master):
        mp.use('TkAgg')
        self.master = master
        master.geometry("800x400")

        self.entry = Entry(master, width=70)
        self.label = Label(master)
        self.button = Button(text="LaTeX!", command=self.graph)

        # Pack everything
        self.entry.pack()
        self.button.pack()
        self.label.pack()

    def graph(self):
        tmptext = self.entry.get()
        tmptext = "$" + tmptext + "$"

        fig = mp.figure.Figure(figsize=(5, 4), dpi=100)
        fig.clear()
        ax = fig.add_subplot(111)

        ax.clear()
        ax.text(0.2, 0.6, tmptext, fontsize=50)

        canvas = FigureCanvasTkAgg(fig, master=self.label)
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        canvas._tkcanvas.pack(side="top", fill="both", expand=True)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        canvas.draw()


if __name__ == '__main__':
    master = Tk()
    root = Root(master)
    master.mainloop()


# sympy latex (RuntimeError: requires latex parser)
"""
from tkinter import *
import sympy as sp
from PIL import Image, ImageTk
from io import BytesIO


class Root:
    def __init__(self, master):
        # Define the main window and the relevant widgets
        self.master = master
        master.geometry("800x300")
        self.strvar = StringVar()
        self.label = Label(master)
        self.entry = Entry(master, textvariable=self.strvar, width=80)
        self.button = Button(text="LaTeX!", command=self.on_latex)
        # The Euler product formula
        self.strvar.set("\prod_{p\,\mathrm{prime}}\frac1{1-p^{-s}} = \sum_{n=1}^\infty \frac1{n^s}")

        # Pack everything
        self.entry.pack()
        self.button.pack()
        self.label.pack()

    def on_latex(self):
        expr = "$\displaystyle " + self.strvar.get() + "$"

        # This creates a ByteIO stream and saves there the output of sympy.preview
        f = BytesIO()
        the_color = "{" + self.master.cget('bg')[1:].upper() + "}"
        sp.preview(expr, euler=False, preamble=r"\documentclass{standalone}"
                                               r"\usepackage{pagecolor}"
                                               r"\definecolor{graybg}{HTML}" + the_color +
                                               r"\pagecolor{graybg}"
                                               r"\begin{document}",
                   viewer="BytesIO", output="ps", outputbuffer=f)
        f.seek(0)
        # Open the image as if it were a file. This works only for .ps!
        img = Image.open(f)
        # See note at the bottom
        img.load(scale=10)
        img = img.resize((int(img.size[0] / 2), int(img.size[1] / 2)), Image.BILINEAR)
        photo = ImageTk.PhotoImage(img)
        self.label.config(image=photo)
        self.label.image = photo
        f.close()


if __name__ == '__main__':
    master = Tk()
    root = Root(master)
    master.mainloop()
"""