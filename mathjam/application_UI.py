import tkinter as tk
from tkinter import simpledialog, messagebox
import tkinter.ttk as ttk
import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import *

from generator import *


class AppFrame:
    def __init__(self, numQ, topic, subtopics: list):
        self.master = tk.Tk()
        self.master.title("Math Jam")
        self.parent = tk.Frame(self.master)
        self.numQ = numQ
        self.topic = topic
        self.subtopics = subtopics

        # build ui
        self.qHeader = ttk.Label(self.master, font="{Ariel} 16 {bold}", text="Question:")
        self.qHeader.grid(column="0", row="0")

        self.updateQuestion()

        self.respHeader = ttk.Label(self.master, font="{Ariel} 16 {bold}", text="Your Response:")
        self.respHeader.grid(column="0", row="3")

        # response plot for displaying response in LaTeX
        respFigure = mp.figure.Figure(figsize=(12, 3), dpi=100)
        respAxis = respFigure.add_subplot(111)
        respAxis.get_xaxis().set_visible(False)
        respAxis.get_yaxis().set_visible(False)
        respCanvas = FigureCanvasTkAgg(respFigure, master=self.master)
        respCanvas.get_tk_widget().grid(column='0', row='4')
        respCanvas.draw()

        self.respFrame = ttk.Frame(self.master)
        self.respFrame.grid(column="0", row="5", pady='10')
        self.respLabel = ttk.Label(self.respFrame, font="{Ariel} 12 {bold}", text="Enter Answer: ")
        self.respLabel.grid(column="0", row="0")
        self.respEntry = ttk.Entry(self.respFrame, width='50')
        self.respEntry.grid(column="1", row="0", ipady='5')
        self.respButton = ttk.Button(self.respFrame, text="Start", command=self.enter)
        self.respButton.grid(column="2", row="0", padx="5", ipadx="10", ipady="5")

    def genQuestion(self):
        # t = self.subtopics[randint(0, len(self.subtopics)-1)]
        t = choice(self.subtopics)
        print(t)
        eq = ""
        func = ""

        if t == "Polynomials":
            func = genRandDegPoly()
        elif t == "Product and Quotient Rule":
            pass
        elif t == "Trig and Inverse Trig":
            pass
        elif t == "Log and Exponential":
            pass
        elif t == "Chain Rule":
            pass
        elif t == "Implicit":
            pass
        elif t == "Inverse":
            pass
        elif t == "U-substitution":
            pass
        elif t == "Integration by Parts":
            pass
        elif t == "Partial Fractions":
            pass
        elif t == "Improper Integrals":
            pass
        print(self.topic)
        if self.topic == 0:  # derivatives
            eq = "Evaluate the following derivative: \n" + r"$\frac{d}{dx}" + f"{func}$"
        elif self.topic == 1:  # indefinite integrals
            eq = "Evaluate the following integral: \n" + r"$\int" + func + r"\, dx$"

        self.updateQuestion(eq)

    def updateQuestion(self, equation=None):
        mp.use('TkAgg')

        qFigure = mp.figure.Figure(figsize=(12, 3), dpi=100)
        qAxis = qFigure.add_subplot(111)
        qAxis.get_xaxis().set_visible(False)
        qAxis.get_yaxis().set_visible(False)

        if equation is not None:
            equation = mathToLatex(equation)
            qAxis.text(0.05, 0.2, equation, fontsize=16)

        qCanvas = FigureCanvasTkAgg(qFigure, master=self.master)
        qCanvas.get_tk_widget().grid(column='0', row='2')
        qCanvas.draw()

    def updateResponse(self, equation=None):
        respFigure = mp.figure.Figure(figsize=(12, 3), dpi=100)
        respAxis = respFigure.add_subplot(111)
        respAxis.get_xaxis().set_visible(False)
        respAxis.get_yaxis().set_visible(False)

        if equation is not None and equation != "":
            equation = "$" + equation.replace("\n", "$\n$") + "$"
            respAxis.text(0.05, 0.2, equation, fontsize=16)
        elif equation is None or equation == "":
            messagebox.showerror("Invalid Response", "Please enter a valid, non-empty response")
            return

        respCanvas = FigureCanvasTkAgg(respFigure, master=self.master)
        respCanvas.get_tk_widget().grid(column='0', row='4')
        respCanvas.draw()

    def enter(self):
        if self.respButton['text'] == "Start":
            self.respButton.configure(text="Enter")
            self.genQuestion()
            return

        self.updateResponse(self.respEntry.get())

    def run(self):
        self.parent.mainloop()


if __name__ == '__main__':
    app = AppFrame(10, 0, ['Polynomials'])
    app.run()
