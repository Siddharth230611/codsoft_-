
from tkinter import *

def press(num):
    expression.set(expression.get() + str(num))

def equalpress():
    try:
        expression.set(str(eval(expression.get())))
    except:
        expression.set("error")

def clear():
    expression.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="#000000")
    gui.title("Simple Calculator")
    gui.geometry("400x580")

    expression = StringVar()
    Entry(gui, textvariable=expression, bg="#98fb98", fg="#000000", font=('Arial', 20)).grid(row=0, column=0, columnspan=4, ipadx=40, ipady=30, padx=5, pady=5)

    buttons = [
        ('C', 1, 0), ('/', 1, 1), ('*', 1, 2), ('-', 1, 3),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
        ('0', 5, 0), ('.', 5, 2), ('=', 4, 3, 2)
    ]

    for button in buttons:
        text, row, col = button[0], button[1], button[2]
        action = lambda x=text: press(x) if x not in ('=', 'C') else (equalpress() if x == '=' else clear())
        if text == '0':
            Button(gui, text=text, fg="#FFFF00", bg="#4682B4", font=('Arial', 14), command=action, height=3, width=16).grid(row=row, column=col, columnspan=2, padx=5, pady=5)
        elif text == '=':
            Button(gui, text=text, fg="#FFFF00", bg="#4682B4", font=('Arial', 14), command=action, height=7, width=7).grid(row=row, column=col, rowspan=2, padx=5, pady=5)
        elif text == '+':
            Button(gui, text=text, fg="#FFFF00", bg="#4682B4", font=('Arial', 14), command=action, height=7, width=7).grid(row=row, column=col, rowspan=2, padx=5, pady=5)
        else:
            Button(gui, text=text, fg="#FFFF00", bg="#4682B4", font=('Arial', 14), command=action, height=3, width=7).grid(row=row, column=col, padx=5, pady=5)

    gui.mainloop()

