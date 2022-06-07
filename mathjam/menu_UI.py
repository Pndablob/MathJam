import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from application_UI import AppFrame


class MenuFrame:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Jam Main Menu")
        self.parent = tk.Frame(self.master)
        self.parent.grid(column='2', row='2', pady='25')
        self.parent.pack(side="top", fill="both", expand=True)

        self.topic = tk.IntVar()
        self.topic.set(-1)
        self.subtopics = []
        self.checked = []
        self.checkButtons = []

        # build ui
        self.topicFrame = ttk.Labelframe(self.parent, height='200', width='200', text='Topic Selection')
        self.topicFrame.grid(column='0', row='0')
        self.derivativeRB = ttk.Radiobutton(self.topicFrame, text="Derivatives", value=0, command=self.derivative, variable=self.topic)
        self.derivativeRB.pack(side='top', fill='both')
        self.indefIntRB = ttk.Radiobutton(self.topicFrame, text='Indefinite Integrals', value=1, command=self.indefIntegral, variable=self.topic)
        self.indefIntRB.pack(side='top', fill='both')
        self.defIntRB = ttk.Radiobutton(self.topicFrame, text='Definite Integrals', value=2, command=self.defIntegral, variable=self.topic)
        self.defIntRB.pack(side='top', fill='both')
        self.typeFrame = ttk.Labelframe(self.parent, height='200', width='200', text='Subtopic Selection')
        self.typeFrame.grid(column='1', row='0')
        self.settingsFrame = ttk.Labelframe(self.parent, height='200', width='200', text='Other Settings')
        self.settingsFrame.grid(column='0', row='1')
        self.numQEntry = ttk.Entry(self.settingsFrame, width='20')
        self.numQEntry.grid(column='1', row='0')
        self.numQLabel = ttk.Label(self.settingsFrame, font="{Ariel} 12 {bold}", text='Number of Questions: ')
        self.numQLabel.grid(column='0', row='0')
        self.startButton = ttk.Button(self.parent, text="Let's Jam!", command=self.start)
        self.startButton.grid(column='1', row='1', ipadx='15')

    def run(self):
        self.parent.mainloop()

    def start(self):
        numQ = self.numQEntry.get()

        # get selected subtopics
        subtopics = []
        for i in range(len(self.checked)):
            v = self.checked[i].get()
            if v == 1:
                subtopics.append(self.subtopics[i])

        # exception handling
        try:
            if len(subtopics) == 0 or self.topic == -1:
                messagebox.showwarning("No Topic Selected", "Please select at least one topic and subtopic")
                return
            elif int(numQ) is None or int(numQ) <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Invalid Number Input", "Please input a valid positive integer number of problems")
            return

        print(subtopics)
        self.master.destroy()

        app = AppFrame(numQ=numQ, topic=self.topic.get(), subtopics=subtopics)
        app.run()

    def displayCheckBox(self, subtopics):
        # clears frame
        for widget in self.typeFrame.winfo_children():
            widget.destroy()
        self.checkButtons = []
        self.checked = []

        for i in range(len(subtopics)):
            self.checked.append(tk.IntVar())
            btn = ttk.Checkbutton(self.typeFrame, text=subtopics[i], variable=self.checked[i])
            self.checkButtons.append(btn)
            self.checked[i].set(0)
            btn.pack(side='top', fill='both')

    # 0
    def derivative(self):
        self.subtopics = [
            "Polynomials",
            "Product and Quotient Rule",
            "Trig and Inverse Trig",
            "Log and Exponential",
            "Chain Rule",
            "Implicit",
            "Inverse"
        ]

        self.displayCheckBox(self.subtopics)

    # 1
    def indefIntegral(self):
        self.subtopics = [
            "Polynomials",
            "U-substitution",
            "Integration by Parts",
            "Partial Fractions"
        ]

        self.displayCheckBox(self.subtopics)

    # 2
    def defIntegral(self):
        self.subtopics = [
            "Improper Integrals"
        ]

        self.displayCheckBox(self.subtopics)



if __name__ == '__main__':
    root = tk.Tk()
    menu = MenuFrame(root)
    menu.run()