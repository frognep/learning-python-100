# Goal: Use Tkinter to create GUI's [Graphic User Interface]

from function import clear
from tkinter import *

clear()

# Creating window
window = Tk()
window.title("First Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Label Example", font=("Arial", "24", "bold"))
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# Loads label onto screen
my_label.pack()

# Entry / Input component
input = Entry()
input.insert(END, string="Insert text here")
input.pack()

def button_click():
    print("I got clicked!")
    my_label.config(text=f"{input.get()}")


button = Button(text="Click Me", command=button_click)
button.pack()


# Always at end of program
window.mainloop()