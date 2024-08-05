from tkinter import *
import random, string

# Initialize the main window
root = Tk()
root.title("Password Generator")
root.geometry("400x280+100+100")
root.resizable(False,False)

# Title Label
title = StringVar()

TopImage = PhotoImage(file="To-Do list/images/top.png")
Label(root, image=TopImage).pack()
heading = Label(root, text="Password Generator", font="arial 20 bold", fg="#FEE715", bg="black")
heading.place(x=30, y=20)
title.set("The strength of password")

# Selection function
def selection():
    pass

# Choice variable for RadioButtons
choice = IntVar()

# RadioButtons for password strength
R1 = Radiobutton(root, text="Poor", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="Average", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="Advanced", variable=choice, value=3, command=selection).pack(anchor=CENTER)

# Label for password length
lenlabel = StringVar()
lenlabel.set("Password Length")
lentitle = Label(root, textvariable=lenlabel).pack()

# Spinbox for selecting password length
val = IntVar()
spinlength = Spinbox(root, from_=8, to_=24, textvariable=val, width=13).pack()

# Password generation function
def passgen():
    poor = string.ascii_uppercase + string.ascii_lowercase
    average = string.ascii_uppercase + string.ascii_lowercase + string.digits
    symbols = """@#&*_."""
    advance = poor + average + symbols
    
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))

# Callback function for button
def callback():
    password.set(passgen())

# Button to generate password
passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()

# Label to display the generated password
password = StringVar()
result_label = Label(root, textvariable=password)
result_label.pack(side=BOTTOM)

# Start the main loop
root.mainloop()
