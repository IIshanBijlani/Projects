from tkinter import *   #import the tkinter module
from functools import partial

def sel(x,y):
    
    y.config(text="Gender is "+str(x.get()))

def main():
    root = Tk() 		#Create an empty window
    var = StringVar(master=None,value="0")    
    label1 = Label(root)
    R1 = Radiobutton(root, text="Male", variable=var, value="Male", command=partial(sel,var,label1))
    R1.pack( anchor = W )
    R2 = Radiobutton(root, text="Female", variable=var, value="Female", command=partial(sel,var,label1))
    R2.pack( anchor = W )
    R3 = Radiobutton(root, text="others", variable=var, value="Others", command=partial(sel,var,label1))
    R3.pack( anchor = W)
    label1.pack()    
    root.mainloop()	#Pause the code and do nothing  

main()
