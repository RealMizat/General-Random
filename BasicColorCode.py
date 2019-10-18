


from tkinter import *
from tkinter import colorchooser

def call_me():
    clr = colorchooser.askcolor(title="select color")
    return(clr)

root = Tk()




button = Button(root, text="change color", command=call_me)
button.pack()
root.geometry("400x400")
root.mainloop(C)