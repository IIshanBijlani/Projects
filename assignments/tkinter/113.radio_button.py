from tkinter import *   #import the tkinter module

def sel():
    label1.config(text="Gender is "+str(var.get()))


root = Tk() 		#Create an empty window
var = IntVar(master=None)    
label1 = Label(root)
R1 = Radiobutton(root, text="Male", variable=var, value=1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Female", variable=var, value=2, command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="others", variable=var, value=3, command=sel)
R3.pack( anchor = W)
label1.pack()    
root.mainloop()	#Pause the code and do nothing  
