import tkinter as tk
import tkinter.ttk as ttk


class AppFrame(tk.Frame):
    def __int__(self, parent):
        super().__init__(self, parent)
        self.parent = parent

        # build ui


if __name__ == '__main__':
    root = tk.Tk()
    AppFrame(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
