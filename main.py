import Tkinter
from Tkinter import *
import tkMessageBox

val = ""
A = 0
operator= ""


def entered_7(event):
    btn7.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_7(event):
    btn7.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_8(event):
    btn8.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_8(event):
    btn8.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_9(event):
    btn9.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_9(event):
    btn9.config(
        bg="#F0F0F0",
        fg="#000000"
    )
def entered_plus(event):
    btn_plus.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_plus(event):
    btn_plus.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_4(event):
    btn4.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_4(event):
    btn4.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_5(event):
    btn5.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_5(event):
    btn5.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_6(event):
    btn6.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_6(event):
    btn6.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_minus(event):
    btn_minus.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_minus(event):
    btn_minus.config(
        bg="#F0F0F0",
        fg="#000000"
    )
def entered_1(event):
    btn1.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_1(event):
    btn1.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_2(event):
    btn2.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_2(event):
    btn2.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_3(event):
    btn3.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_3(event):
    btn3.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_multi(event):
    btn_multi.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_multi(event):
    btn_multi.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_clear(event):
    btn_clear.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_clear(event):
    btn_clear.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_zero(event):
    btn_zero.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_zero(event):
    btn_zero.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_result(event):
    btn_result.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_result(event):
    btn_result.config(
        bg="#F0F0F0",
        fg="#000000"
    )

def entered_division(event):
    btn_division.config(
        bg="#C9C9C9",
        fg="#ffffff"
    )
def left_division(event):
    btn_division.config(
        bg="#F0F0F0",
        fg="#000000"
    )













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
btn7.bind("<Enter>", entered_7)
btn7.bind("<Leave>", left_7)

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
btn8.bind("<Enter>", entered_8)
btn8.bind("<Leave>", left_8)

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
btn9.bind("<Enter>", entered_9)
btn9.bind("<Leave>", left_9)

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
btn_plus.bind("<Enter>", entered_plus)
btn_plus.bind("<Leave>", left_plus)

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
btn4.bind("<Enter>", entered_4)
btn4.bind("<Leave>", left_4)

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
btn5.bind("<Enter>", entered_5)
btn5.bind("<Leave>", left_5)

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
btn6.bind("<Enter>", entered_6)
btn6.bind("<Leave>", left_6)

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
btn_minus.bind("<Enter>", entered_minus)
btn_minus.bind("<Leave>", left_minus)

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
btn1.bind("<Enter>", entered_1)
btn1.bind("<Leave>", left_1)


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
btn2.bind("<Enter>", entered_2)
btn2.bind("<Leave>", left_2)

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
btn3.bind("<Enter>", entered_3)
btn3.bind("<Leave>", left_3)

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
btn_multi.bind("<Enter>", entered_multi)
btn_multi.bind("<Leave>", left_multi)

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
btn_clear.bind("<Enter>", entered_clear)
btn_clear.bind("<Leave>", left_clear)

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
btn_zero.bind("<Enter>", entered_zero)
btn_zero.bind("<Leave>", left_zero)

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
btn_result.bind("<Enter>", entered_result)
btn_result.bind("<Leave>", left_result)

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
btn_division.bind("<Enter>", entered_division)
btn_division.bind("<Leave>", left_division)

root.mainloop()
