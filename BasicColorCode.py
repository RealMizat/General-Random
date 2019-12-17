


from tkinter import *
from tkinter import colorchooser

def call_me():
    clr = colorchooser.askcolor(title="select color")
    return(clr)


root = Tk()


#I found another version with  __name__ = __main__ 
#how ever I do not fully understand understand how that works, I get what it does, just not why, so Istay away from it for now.


button = Button(root, text="change color", command=call_me)
button.pack()
root.geometry("400x400")
root.mainloop()

#I would be very interested in other scripts that use this dialog, or even better, create their own color picker
#so if you know of any open source code, or even code that is avaible to view that either uses the color chooser 
#dialog, or that uses their own color chooser (created from scratch or even another module) I would love to look at it
#as far as I can tell there is not much code at all avaible using the color chooser dilog, and even less python created
#color choosers. This is something I am looking to intergrate into a GUI, and it is a main function, however myself cannot
#find the material.

#As for the code above, the color or clr returns a tuple, so that tuple would need to be changed to a list, because the 
#fotmat the tuple returns the color in is RBG and hex, hex would need to be takenout, or vice versa, depending on how you
#want to format color numbers ect. I would use list(clr) to simply turn it into a list and then go from there.
