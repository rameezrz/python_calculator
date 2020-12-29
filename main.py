import Tkinter
from Tkinter import *
import tkMessageBox

val = ""
A = 0
operator= ""


def btn_1_is_clicked():
    global val
    val = val + "1"
    data.set(val)


def btn_2_is_clicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_is_clicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_is_clicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_is_clicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_is_clicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_is_clicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_is_clicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_is_clicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_is_clicked():
    global val
    val = val + "0"
    data.set(val)

def btn_plus_is_clicked():
    global A
    global val
    global operator
    A = int(val)
    operator = "+"
    val=val + "+"
    data.set(val)


def btn_minus_is_clicked():
    global A
    global val
    global operator
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_multi_is_clicked():
    global A
    global val
    global operator
    A = int(val)
    operator = "x"
    val = val + "x"
    data.set(val)

def btn_div_is_clicked():
    global A
    global val
    global operator
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_clear_is_clicked():
    global A
    global operator
    global val
    A = 0
    operator = ""
    val= ""
    data.set(val)

def btn_result_is_clicked():
    global A
    global operator
    global val
    val2=val
    if operator == "+":
        x = int(val2.split("+")[1])
        result = A + x
        data.set(result)
        val = str(result)
    elif operator == "-":
        x = int(val2.split("-")[1])
        result = A - x
        data.set(result)
        val = str(result)
    elif operator == "x":
        x = int(val2.split("x")[1])
        result = A * x
        data.set(result)
        val = str(result)
    elif operator == "/":
        x = int(val2.split("/")[1])
        if x == 0:
            tkMessageBox.showerror("Error","Cannot devided by Zero")
            A = ""
            val = ""
            data.set(val)
        else:
            result = int(A / x)
            data.set(result)
            val = str(result)


root = Tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0, 0)
root.title("Calculator")

data = StringVar()
lbl = Label(
    root, text="Label",
    anchor=SE,
    font=('Verdana', 20),
    textvariable=data,
    background="#ffffff",
    foreground="#000000")
lbl.pack(
    expand=True, fill='both'
)

btn_row_1 = Frame(root)
btn_row_1.pack(expand=True, fill="both", )

btn_row_2 = Frame(root)
btn_row_2.pack(expand=True, fill="both", )

btn_row_3 = Frame(root)
btn_row_3.pack(expand=True, fill="both", )

btn_row_4 = Frame(root)
btn_row_4.pack(expand=True, fill="both", )

btn7 = Button(
    btn_row_1,
    text="7",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_7_is_clicked(),
)
btn7.pack(
    side=LEFT, expand=True, fill='both'
)

btn8 = Button(
    btn_row_1,
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_8_is_clicked(),
)
btn8.pack(
    side=LEFT, expand=True, fill='both'
)

btn9 = Button(
    btn_row_1,
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_9_is_clicked(),
)
btn9.pack(
    side=LEFT, expand=True, fill='both'
)

btn_plus = Button(
    btn_row_1,
    text="+",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_plus_is_clicked(),
)
btn_plus.pack(
    side=LEFT, expand=True, fill='both'
)

btn4 = Button(
    btn_row_2,
    text="4",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_4_is_clicked(),
)
btn4.pack(
    side=LEFT, expand=True, fill='both'
)

btn5 = Button(
    btn_row_2,
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_5_is_clicked(),
)
btn5.pack(
    side=LEFT, expand=True, fill='both'
)

btn6 = Button(
    btn_row_2,
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_6_is_clicked(),
)
btn6.pack(
    side=LEFT, expand=True, fill='both'
)

btn_minus = Button(
    btn_row_2,
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_minus_is_clicked(),
)
btn_minus.pack(
    side=LEFT, expand=True, fill='both'
)

btn1 = Button(
    btn_row_3,
    text="1",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_1_is_clicked(),
)
btn1.pack(
    side=LEFT, expand=True, fill='both',
)

btn2 = Button(
    btn_row_3,
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_2_is_clicked(),
)
btn2.pack(
    side=LEFT, expand=True, fill='both'
)

btn3 = Button(
    btn_row_3,
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_3_is_clicked(),
)
btn3.pack(
    side=LEFT, expand=True, fill='both'
)

btn_multi = Button(
    btn_row_3,
    text="x",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_multi_is_clicked(),
)
btn_multi.pack(
    side=LEFT, expand=True, fill='both'
)

btn_clear = Button(
    btn_row_4,
    text="C",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_clear_is_clicked(),
)
btn_clear.pack(
    side=LEFT, expand=True, fill='both'
)

btn_zero = Button(
    btn_row_4,
    text="0",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_0_is_clicked()

)
btn_zero.pack(
    side=LEFT, expand=True, fill='both'
)

btn_result = Button(
    btn_row_4,
    text="=",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_result_is_clicked(),
)
btn_result.pack(
    side=LEFT, expand=True, fill='both'
)

btn_division = Button(
    btn_row_4,
    text="/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= lambda: btn_div_is_clicked(),
)
btn_division.pack(
    side=LEFT, expand=True, fill='both'
)

root.mainloop()
