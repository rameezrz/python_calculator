import Tkinter
from Tkinter import *

root=Tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

lbl=Label(
    root, text="Label", anchor=SE, font=('Verdana', 20)
)
lbl.pack(
    expand=True, fill='both'
)

btn_row_1= Frame(root)
btn_row_1.pack(expand=True, fill="both",)

btn_row_2= Frame(root)
btn_row_2.pack(expand=True, fill="both",)

btn_row_3= Frame(root)
btn_row_3.pack(expand=True, fill="both",)

btn_row_4= Frame(root)
btn_row_4.pack(expand=True, fill="both",)

btn7=Button(
    btn_row_1,
    text="7",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn7.pack(
    side=LEFT, expand=True, fill='both'
)

btn8=Button(
    btn_row_1,
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn8.pack(
    side=LEFT, expand=True, fill='both'
)

btn9=Button(
    btn_row_1,
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn9.pack(
    side=LEFT, expand=True, fill='both'
)

btn_plus=Button(
    btn_row_1,
    text="+",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn_plus.pack(
    side=LEFT, expand=True, fill='both'
)






btn4=Button(
    btn_row_2,
    text="4",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn4.pack(
    side=LEFT, expand=True, fill='both'
)

btn5=Button(
    btn_row_2,
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn5.pack(
    side=LEFT, expand=True, fill='both'
)

btn6=Button(
    btn_row_2,
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn6.pack(
    side=LEFT, expand=True, fill='both'
)

btn_minus=Button(
    btn_row_2,
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn_minus.pack(
    side=LEFT, expand=True, fill='both'
)






btn1=Button(
    btn_row_3,
    text="1",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn1.pack(
    side=LEFT, expand=True, fill='both'
)

btn2=Button(
    btn_row_3,
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn2.pack(
    side=LEFT, expand=True, fill='both'
)

btn3=Button(
    btn_row_3,
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn3.pack(
    side=LEFT, expand=True, fill='both'
)

btn_multi=Button(
    btn_row_3,
    text="x",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn_multi.pack(
    side=LEFT, expand=True, fill='both'
)





btn_clear=Button(
    btn_row_4,
    text="C",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn_clear.pack(
    side=LEFT, expand=True, fill='both'
)

btn_zero=Button(
    btn_row_4,
    text="0",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn_zero.pack(
    side=LEFT, expand=True, fill='both'
)

btn_result=Button(
    btn_row_4,
    text="=",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn_result.pack(
    side=LEFT, expand=True, fill='both'
)

btn_division=Button(
    btn_row_4,
    text="/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0
)
btn_division.pack(
    side=LEFT, expand=True, fill='both'
)

root.mainloop()