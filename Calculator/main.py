import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("370x540+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

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

Button(root,text="C",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#708090", command=lambda: clear()).place(x=10,y=110)
Button(root,text="%",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#36454F", command=lambda: show("%")).place(x=100,y=110)
Button(root,text="/",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#36454F", command=lambda: show("/")).place(x=190,y=110)
Button(root,text="x",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#36454F", command=lambda: show("*")).place(x=280,y=110)

Button(root,text="7",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("7")).place(x=10,y=195)
Button(root,text="8",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("8")).place(x=100,y=195)
Button(root,text="9",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("9")).place(x=190,y=195)
Button(root,text="-",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#36454F", command=lambda: show("-")).place(x=280,y=195)

Button(root,text="4",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("4")).place(x=10,y=280)
Button(root,text="5",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("5")).place(x=100,y=280)
Button(root,text="6",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("6")).place(x=190,y=280)
Button(root,text="+",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#36454F", command=lambda: show("+")).place(x=280,y=280)

Button(root,text="1",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("1")).place(x=10,y=365)
Button(root,text="2",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("2")).place(x=100,y=365)
Button(root,text="3",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("3")).place(x=190,y=365)
Button(root,text=".",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#36454F", command=lambda: show(".")).place(x=280,y=365)

Button(root,text="00",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("00")).place(x=10,y=450)
Button(root,text="0",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#696969", command=lambda: show("0")).place(x=100,y=450)
Button(root,text="=",width=7, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#708090", command=lambda: calculate()).place(x=190,y=450)

root.mainloop()