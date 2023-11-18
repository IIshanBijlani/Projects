from tkinter import *   #import the tkinter module
from functools import partial

def sel(x,y):
    
    y.config(text="Gender is "+str(x.get()))

def main():
    root = Tk() 		#Create an empty window
    var = IntVar(master=None)    
    label1 = Label(root)
    R1 = Radiobutton(root, text="Male", variable=var, value="1",indicator=2, command=partial(sel,var,label1))
    R1.pack( anchor = W )
    R2 = Radiobutton(root, text="Female", variable=var, value="2", command=partial(sel,var,label1))
    R2.pack( anchor = W )
    R3 = Radiobutton(root, text="others", variable=var, value="3", command=partial(sel,var,label1))
    R3.pack( anchor = W)
    label1.pack()    
    root.mainloop()	#Pause the code and do nothing  

main()