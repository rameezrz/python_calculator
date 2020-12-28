import Tkinter
from Tkinter import *

root=Tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

btn_row_1= Frame(root, bg='#000000')
btn_row_1.pack(expand=True, fill="both",)

root.mainloop()