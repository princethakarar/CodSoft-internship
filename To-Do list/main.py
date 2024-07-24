import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("To-Do List")
root.geometry("400x580+400+100")
root.resizable(False, False)

task_list = []

def editTask():
    task = listbox.get(ANCHOR)
    if task:
        task_entry.delete(0, END)
        task_entry.insert(0, task)
        deleteTask()  # Remove the task to avoid duplication

def deleteTask():
    global task_list
    task = listbox.get(ANCHOR)
    if task in task_list:
        task_list.remove(task)
        with open("To-Do list/task.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        
        listbox.delete(ANCHOR)

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("To-Do list/task.txt", "a") as textfile:
            textfile.write(task + "\n")
        task_list.append(task)
        listbox.insert(END, task)

def openTaskFile():
    try:
        global task_list
        with open("To-Do list/task.txt") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            task = task.strip()  # Remove newline characters
            if task:  # Ensure the task is not an empty string
                task_list.append(task)
                listbox.insert(END, task)
    except FileNotFoundError:
        with open("To-Do list/task.txt", "w") as file:
            pass  # Just create the file if it doesn't exist

# icon

Image_icon = PhotoImage(file="To-Do list/images/task.png")
root.iconphoto(False, Image_icon)

# top bar

TopImage = PhotoImage(file="To-Do list/images/top.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="To-Do list/images/dock.png")
Label(root, image=dockImage, bg="black").place(x=30, y=25)

noteImage = PhotoImage(file="To-Do list/images/task.png")
Label(root, image=noteImage, bg="black").place(x=340, y=25)

heading = Label(root, text="To-Do List", font="arial 20 bold", fg="#FEE715", bg="black")
heading.place(x=130, y=20)

# main

frame = Frame(root, width=400, height=50, bg="white", borderwidth=2)
frame.place(x=0, y=110)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="Add", font="arial 20 bold", width=6, bg="black", fg="#FEE715", bd=0, command=addTask)
button.place(x=300, y=0)

# listbox

frame1 = Frame(root, bd=3, width=700, height=280, bg="black")
frame1.pack(pady=(90, 0))  # Adjust the pady value to 70 to set the spacing

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="black", fg="#FEE715", cursor="hand2", selectbackground="#FBF4B5", selectforeground="black")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# button frame

button_frame = Frame(root)
button_frame.pack(side=BOTTOM, pady=20)

# delete button

Delete_icon = PhotoImage(file="To-Do list/images/delete3.png")
delete_button = Button(button_frame, image=Delete_icon, bd=0, command=deleteTask)
delete_button.pack(side=LEFT, padx=10)

# edit button

# Resize the image using PIL
edit_image = Image.open("To-Do list/images/edit.png")
edit_image = edit_image.resize((50, 50), Image.LANCZOS)
Edit_icon = ImageTk.PhotoImage(edit_image)

edit_button = Button(button_frame, image=Edit_icon, bd=0, command=editTask)
edit_button.pack(side=LEFT, padx=10)

root.mainloop()