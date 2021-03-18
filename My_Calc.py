import tkinter as tk
from tkinter import *
from tkinter import messagebox

val = ""


def btn_1_isClicked():
    global val;
    val = val + "1"
    lbl_data.set(val)


def btn_2_isClicked():
    global val;
    val = val + "2"
    lbl_data.set(val)


def btn_3_isClicked():
    global val;
    val = val + "3"
    lbl_data.set(val)


def btn_4_isClicked():
    global val;
    val = val + "4"
    lbl_data.set(val)


def btn_5_isClicked():
    global val;
    val = val + "5"
    lbl_data.set(val)


def btn_6_isClicked():
    global val;
    val = val + "6"
    lbl_data.set(val)


def btn_7_isClicked():
    global val;
    val = val + "7"
    lbl_data.set(val)


def btn_8_isClicked():
    global val;
    val = val + "8"
    lbl_data.set(val)


def btn_9_isClicked():
    global val;
    val = val + "9"
    lbl_data.set(val)


def btn_0_isClicked():
    global val;
    val = val + "0"
    lbl_data.set(val)


def btn_plus_isClicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    lbl_data.set(val)


def btn_sub_isClicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    lbl_data.set(val)


def btn_mult_isClicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    lbl_data.set(val)


def btn_div_isClicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    lbl_data.set(val)


def c_isClicked():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    lbl_data.set(val)


def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        lbl_data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        lbl_data.set(c)
        val = str(c)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        lbl_data.set(c)
        val = str(c)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division by 0 Not Allowed")
            A = ""
            val = ""
            lbl_data.set(val)
        else:
            c = float(A / x)
            lbl_data.set(c)
            val = str(c)


root = tk.Tk()
root.geometry("300x400+300+300")
root.resizable(0, 0)

root.title("My Calculator")
lbl_data = StringVar()

l1 = Label(root, text="Label", anchor=SE, font=("Verdana", 20), textvariable=lbl_data, background="#ffffff",
           fg='#000000')
l1.pack(expand=True, fill="both")

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root, bg="")
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root, bg="")
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root, bg="")
btnrow4.pack(expand=True, fill="both")

btn1 = Button(
    btnrow1,
    text="1",
    font=("Verdana", 20),
    relief=GROOVE,
    border=0,
    command=btn_1_isClicked
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_2_isClicked
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_3_isClicked
)
btn3.pack(side=LEFT, expand=True, fill="both")

btnplus = Button(
    btnrow1,
    text="+",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_plus_isClicked
)
btnplus.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow2,
    text="4",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_4_isClicked
)
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    btnrow2,
    text="5",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_4_isClicked
)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    btnrow2,
    text="6",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_5_isClicked
)
btn6.pack(side=LEFT, expand=True, fill="both")

btnsub = Button(
    btnrow2,
    text="-",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_sub_isClicked
)
btnsub.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(
    btnrow3,
    text="7",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_7_isClicked
)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    btnrow3,
    text="8",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_8_isClicked
)
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    btnrow3,
    text="9",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_9_isClicked
)
btn9.pack(side=LEFT, expand=True, fill="both")

btnmult = Button(
    btnrow3,
    text="*",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_mult_isClicked
)
btnmult.pack(side=LEFT, expand=True, fill="both")

btnc = Button(
    btnrow4,
    text="C",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=c_isClicked

)
btnc.pack(side=LEFT, expand=True, fill="both")

btn0 = Button(
    btnrow4,
    text="0",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_0_isClicked
)
btn0.pack(side=LEFT, expand=True, fill="both")

btnequal = Button(
    btnrow4,
    text="=",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=result
)
btnequal.pack(side=LEFT, expand=True, fill="both")

btndiv = Button(
    btnrow4,
    text="/",
    font=("Verdana", 20), relief=GROOVE,
    border=0,
    command=btn_div_isClicked
)
btndiv.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
