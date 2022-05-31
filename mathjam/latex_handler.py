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
