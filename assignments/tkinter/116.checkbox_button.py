from tkinter import *   #import the tkinter module
from functools import partial

def sel(x,y):
    values=["PHP","Python","Perl"]
    i=0
    s=""
    for z in x:
        #print(z.get())
        if int(z.get())==1:
            s=s+values[i]+" "
        i=i+1
    y.config(text="Selection is "+s)

def main():
    root = Tk() 		#Create an empty window
    root.geometry("400x300")
    var1 = StringVar(master=None,value="0")    
    var2 = StringVar(master=None,value="0")    
    var3 = StringVar(master=None,value="0") 
    var=[var1,var2,var3]
    label1 = Label(root)
    R1 = Checkbutton(root, text="PHP", variable=var1,  command=partial(sel,var,label1))
    R1.pack( anchor = W )
    R2 = Checkbutton(root, text="Python", variable=var2,  command=partial(sel,var,label1))
    R2.pack( anchor = W )
    R3 = Checkbutton(root, text="Perl", variable=var3,  command=partial(sel,var,label1))
    R3.pack( anchor = W)
    label1.pack()    
    root.mainloop()	#Pause the code and do nothing  

main()
