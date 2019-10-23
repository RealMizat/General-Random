


from tkinter import *
from tkinter import colorchooser

def call_me():
    clr = colorchooser.askcolor(title="select color")
    return(clr)

#need class for windows or frames that will take that color (sub-class)
#anyone whom comes across this feel free to help I'm new trying to create 
#Either frames or Canvas' that fill to the colors choosen and ability to save 
#Those colors or an image with color numbers, so I need to pass the RGB values from the output 
#witch is a tuple, or the last value 4rd value in HEX to create the color
#The easiest way I think would be to draw a very thick line so it's a square or close to it
#Grid is probbaly going to be used, at least with my logic it should work, however I am probably wrong

#Please help if you come across this, still trying to graspe class' and methods and all the different types, syntax and rules
#There is so much to them, and never have created my own yet, like i'm attempting here.

root = Tk()


I found another version with the __name__ = __main__ or a couple
#how ever I do not fully understand that, even though I have read up on it quit a bit
#I would not be able to put it into anything I come up with 100% on my own
#   So for now would like to leave it out.

button = Button(root, text="change color", command=call_me)
button.pack()
root.geometry("400x400")
root.mainloop()

#if anyone comes across this and don't feel like helping, however know a guide or tutorial that will help
#maybe a similar tk or even wx code, either with a guide or tutorial or not please let me know
