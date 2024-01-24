from function import clear
import tkinter

clear()

window = tkinter.Tk()
window.title("Calculator")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)


# User's Mile Input
input = tkinter.Entry(width=10)
input.grid(column=2, row=1)

# Miles label
miles_label = tkinter.Label(text="Miles", font=("Arial", 18) )
miles_label.grid(column=3, row=1)

# Line 2 label
is_equal_to_label = tkinter.Label(text="is equal to", font=("Arial", 18) )
is_equal_to_label.grid(column=1, row=2)

# Answer
answer = tkinter.Label(text="0", font=("Arial", 18) )
answer.grid(column=2, row=2)

# Unit label
unit = tkinter.Label(text="KM", font=("Arial", 18) )
unit.grid(column=3, row=2)

def button_click():
    answer.config(text=f"{float(input.get())*1.6}")
    return (type(input.get()))

# Button
button = tkinter.Button(text="Calculate", command=button_click)
button.grid(column=2, row=3)

window.mainloop()