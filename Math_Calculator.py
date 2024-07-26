"""Homework question
● Himanshi learned about entry widgets and text variables in python Tkinter. She thinks that she can
create a basic calculator using an entry widget, eval function, and a single button. But she is not able
to execute her idea. To help Himanshi, write a program in python to create a simple calculator as given
below.
● Hint:
● Use eval() function to get the answer of the given expression
● Use .set() method to show the answer on entry widget
"""

from tkinter import*
root = Tk()
root.title("Math Calculator")
root.config(bg = "Blue")
def calculate():
    value = expression.get()
    answer = eval(value)
    expression.set(answer)

expression = StringVar()
expressionW = Entry(root , font=("Arial Narrow" , 30), bg="cyan", relief="solid", borderwidth=10 , textvariable=expression)
expressionW.pack()
button = Button(text="Calculate" , font=("Arial Narrow", 30), fg="brown" , bg="yellow", relief="raised" , borderwidth=10 , command=calculate)
button.pack(pady = 30)



root.mainloop()