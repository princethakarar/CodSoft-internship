import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("370x540+100+200")
root.resizable(False,False)
root.configure(bg="#2a2d36")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
        equation = ""
        show(str(result))
    label_result.config(text=result)

label_result = Label(root,width=25,height=2,text="",font=('arial',30), anchor='e')
label_result.pack()

button_colors = {
    "C": "#708090",     # Slate Grey
    "%": "#36454F",     # Dark Teal
    "/": "#36454F",     # Charcoal Grey
    "x": "#36454F",     # Charcoal Grey
    "7": "#696969",     # Dim Grey
    "8": "#696969",     # Dim Grey
    "9": "#696969",     # Dim Grey
    "-": "#36454F",     # Charcoal Grey
    "4": "#696969",     # Dim Grey
    "5": "#696969",     # Dim Grey
    "6": "#696969",     # Dim Grey
    "+": "#36454F",     # Charcoal Grey
    "1": "#696969",     # Dim Grey
    "2": "#696969",     # Dim Grey
    "3": "#696969",     # Dim Grey
    ".": "#36454F",     # Charcoal Grey
    "00": "#696969",    # Dim Grey
    "0": "#696969",     # Dim Grey
}

button_texts = [
    ("C", 10, 110), ("%", 100, 110), ("/", 190, 110), ("x", 280, 110),
    ("7", 10, 195), ("8", 100, 195), ("9", 190, 195), ("-", 280, 195),
    ("4", 10, 280), ("5", 100, 280), ("6", 190, 280), ("+", 280, 280),
    ("1", 10, 365), ("2", 100, 365), ("3", 190, 365), (".", 280, 365),
    ("00", 10, 450), ("0", 100, 450)
]

for (text, x, y) in button_texts:
    bg_color = button_colors[text]
    Button(root, text=text, width=3, height=1 if text != "=" else 2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg=bg_color, command=lambda t=text: show(t) if t != "=" else calculate()).place(x=x, y=y)

Button(root,text="=",width=7, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#708090", command=lambda: calculate()).place(x=190,y=450)    #Slate Grey

root.mainloop()