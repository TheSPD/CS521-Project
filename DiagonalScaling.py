import Tkinter as Tk
import createGrid as cG
import numpy as np


def show_entry_fields():
    Q = np.array([[e1.get(), e2.get()], [e3.get(), e4.get()]],
                 dtype=np.float64)
    cG.plotGrid(Q, master)
# print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk.Tk()
master.wm_title("Diagonal Scaling")
Tk.Label(master, text="Enter a 2x2 PSD : ").grid(row=0)

e1 = Tk.Entry(master)
e2 = Tk.Entry(master)
e3 = Tk.Entry(master)
e4 = Tk.Entry(master)

e1.grid(row=1, column=0)
e2.grid(row=1, column=1)
e3.grid(row=2, column=0)
e4.grid(row=2, column=1)

Tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=Tk.W, pady=4)
Tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=Tk.W, pady=4)

Tk.mainloop()