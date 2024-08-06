from tkinter import *
import random, string

root = Tk()
root.title("Password Generator")
root.geometry("400x280+100+100")
root.resizable(False,False)
root.configure(bg="black")

# Title
title = StringVar()
heading = Label(root, text="Password Generator", font="arial 20 bold", fg="#FEE715", bg="black")
heading.place(x=63, y=10)

def selection():
    pass

choice = IntVar()
R1 = Radiobutton(root, text="Poor", variable=choice, value=1, command=selection, font="arial 11 bold", fg="#FEE715", bg="black").place(x=166,y=50)
R2 = Radiobutton(root, text="Average", variable=choice, value=2, command=selection, font="arial 11 bold", fg="#FEE715", bg="black").place(x=159,y=70)
R3 = Radiobutton(root, text="Advanced", variable=choice, value=3, command=selection, font="arial 11 bold", fg="#FEE715", bg="black").place(x=152,y=90)
 
lenLabel = Label(root, text="Password Length", font="arial 15 bold", fg="#FEE715", bg="black")
lenLabel.place(x=118, y=120)

val = IntVar()
spinlength = Spinbox(root, from_=6, to_=15, textvariable=val, width=13, font="arial 10 bold", fg="#FEE715", bg="black").place(x=150,y=150)

def passgen():
    poor = string.ascii_uppercase + string.ascii_lowercase
    average = string.ascii_uppercase + string.ascii_lowercase + string.digits
    symbols = """@#&*_.!<>$%*-+=,?/"""
    advance = poor + average + symbols
    
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))

def callback():
    password.set(passgen())

passgenButton = Button(root, text="Generate Password", bd=5, height=2, pady=3, width=18, font="arial 10 bold", fg="#FEE715", bg="black", command=callback)
passgenButton.place(x=125,y=200)

password = StringVar()
result_label = Label(root, textvariable=password, font="arial 10 bold", fg="#FEE715", bg="black")
result_label.pack(side=BOTTOM)

root.mainloop()
