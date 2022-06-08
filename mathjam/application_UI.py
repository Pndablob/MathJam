import sys
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from random import *

from generator import *
from utils import *


class AppFrame:
    def __init__(self, numQ, topic, subtopics: list):
        # vars
        self.numQ = numQ
        self.completed = 0
        self.topic = topic
        self.subtopics = subtopics
        self.func = ""
        self.a = 0
        self.b = 0

        # build ui
        self.master = tk.Tk()
        self.master.title("Math Jam")
        self.master.geometry("1200x780")
        self.master.minsize(1200, 780)
        self.parent = tk.Frame(self.master)

        # resize widgets dynamically to frame size
        self.master.columnconfigure(0, weight=1)
        for r in range(self.master.grid_size()[1]):
            self.master.rowconfigure(r, weight=1)

        self.qHeader = ttk.Label(self.master, font="{Ariel} 18 {bold}", text="Question:")
        self.qHeader.grid(column="0", row="0", pady="10")

        # question plot for displaying questions in LaTeX
        updateCanvas(col=0, row=1, master=self.master)

        self.respHeader = ttk.Label(self.master, font="{Ariel} 18 {bold}", text="Your Response:")
        self.respHeader.grid(column="0", row="2", pady="10")

        # response plot for displaying response in LaTeX
        updateCanvas(col=0, row=3, master=self.master)

        self.respFrame = ttk.Frame(self.master)
        self.respFrame.grid(column="0", row="4", pady='20')
        self.respLabel = ttk.Label(self.respFrame, font="{Ariel} 12 {bold}", text="Enter Answer: ")
        self.respLabel.grid(column="0", row="0")
        self.respEntry = ttk.Entry(self.respFrame, width='60', font="10")
        self.respEntry.grid(column="1", row="0", ipady='5')
        self.respButton = ttk.Button(self.respFrame, text="Start", command=self.render)
        self.respButton.grid(column="2", row="0", padx="5", ipadx="10", ipady="5")
        self.nextButton = ttk.Button(self.respFrame, text="Answer", state='disabled', command=self.next)
        self.nextButton.grid(column="3", row="0", padx=(100, 10), ipady="5", ipadx="10")

    def genQuestion(self):
        if self.completed == self.numQ:
            messagebox.showinfo("Study Session Complete",
                                f"Congratulations, you have completed your study session of {self.numQ} problems. Enjoy your break!")
            self.master.destroy()
            sys.exit()

        t = choice(self.subtopics)
        eq = ""
        self.func = ""

        if t == "Polynomials":
            self.func = genRandDegPoly(1, 5)
        elif t == "Chain Rule":
            self.func = genSimpleChain()
        elif t == "Product and Quotient":
            pass
        elif t == "Trigonometric":
            pass
        elif t == "Log and Exponential":
            pass
        elif t == "Partial Fractions":
            pass

        if self.topic == 0:  # derivatives
            eq = "Find the derivative of the following function: \n" + f"${self.func}$"
        elif self.topic == 1:  # indefinite integrals
            eq = "Evaluate the following integral: \n" + r"$\int " + self.func + r" \, dx$"
        elif self.topic == 2:  # definite integrals
            self.a = randint(-5, 0)
            self.b = randint(self.a, 5)
            eq = "Evaluate the following integral: \n" + r"$\int_{" + str(self.a) + "}^{" + str(
                self.b) + "} " + self.func + r" \, dx$"

        updateCanvas(col=0, row=1, master=self.master, equation=eq)

    def render(self):
        if self.respButton['text'] == "Start":
            self.nextButton.configure(state="active")
            self.respButton.configure(text="Render")
            self.genQuestion()
            return

        eq = self.respEntry.get()
        if eq.startswith(" ") and eq.endswith(" ") or eq == "":
            messagebox.showerror("Invalid Response",
                                 "Please do not start and end with spaces. Try again and enter a valid, non-empty response.")
            return

        eq = "$" + eq.replace("\n", "$\n$") + "$"
        updateCanvas(col=0, row=3, master=self.master, equation=eq)

    def next(self):
        eq = self.respEntry.get()
        if eq.startswith(" ") and eq.endswith(" ") or eq == "":
            messagebox.showerror("Invalid Response",
                                 "Please do not start and end with spaces. Try again and enter a valid, non-empty response.")
            return

        updateCanvas(col=0, row=3, master=self.master, equation="$" + eq.replace("\n", "$\n$") + "$")

        ans = ""
        if self.topic == 0:
            ans = getDerivative(self.func)
        elif self.topic == 1:
            ans = getIndefIntegral(self.func)

        giveup = False
        if not self.checkAnswer(equation=eq, answer=ans):
            retry = messagebox.askyesno("Incorrect Answer", "Would you like to try again?", icon='warning')
            if retry:
                return
            giveup = True

        self.showAnswer(answer=ans, giveup=giveup)

    def checkAnswer(self, equation, answer):
        equation = equation.replace(" +", "+").replace("+ ", "+").replace(" -", "-").replace("- ", "-").replace(" /",
                                                                                                                "/").replace(
            "/ ", "/")
        equation = equation.replace("+", " + ").replace("-", " - ")

        equation = equation.replace("+ ", "+").replace("- ", "-")
        resp = equation.split()
        answer = answer.replace("+ ", "+").replace("- ", "-")
        ans = answer.split()

        for a in ans:
            if a not in resp:
                return False
        return True

    def showAnswer(self, answer, giveup):
        def close():
            # reset window and generate new question
            ansMaster.destroy()

            self.respEntry.delete(0, tk.END)
            updateCanvas(col=0, row=1, master=self.master)
            updateCanvas(col=0, row=3, master=self.master)
            self.completed += 1
            self.genQuestion()

        ansMaster = tk.Tk()
        ansMaster.geometry("800x400")
        ansMaster.minsize(800, 400)
        ansMaster.columnconfigure(0, weight=1)
        for r in range(ansMaster.grid_size()[1]):
            ansMaster.rowconfigure(r, weight=1)
        title = ttk.Label(ansMaster, font="{Ariel} 18 {bold}", text="Answer")
        title.grid(column=0, row=0, pady=10)
        continueButton = ttk.Button(ansMaster, text="Continue", command=close)
        continueButton.grid(column=0, row=2, pady=10, ipadx=20)

        if giveup:
            ansMaster.title("You Gave Up")
            title.configure(foreground="red")
        else:
            ansMaster.title("You Were Correct")
            title.configure(foreground="green")

        # show answer in latex
        answer = f"${mathToLatex(answer)}$"
        updateCanvas(col=0, row=1, master=ansMaster, equation=answer)
        ansMaster.mainloop()

    def run(self):
        self.parent.mainloop()


if __name__ == '__main__':
    app = AppFrame(10, 0, ['Polynomials'])
    app.run()
