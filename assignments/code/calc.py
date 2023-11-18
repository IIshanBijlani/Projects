import tkinter as tk

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b 
    d="Sum of given numbers is "+str(c)
    label3.config(text=d)

def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b 
    d="difference of given numbers is "+str(c)
    label3.config(text=d)
def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b 
    d="Product of given numbers is "+str(c)
    label3.config(text=d)
def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b 
    d="Quotient of division is "+str(c)
    label3.config(text=d)
def fdiv():
    a=int(e1.get())
    b=int(e2.get())
    c=a//b 
    d="Floor Quotient of division is "+str(c)
    label3.config(text=d)
def exp():
    a=int(e1.get())
    b=int(e2.get())
    c=a**b 
    d="Power  is "+str(c)
    label3.config(text=d)


root = tk.Tk()
label1=tk.Label(root,text="Enter first number")
label1.grid(row=0)
label2=tk.Label(root,text="Enter Second number")
label2.grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

label3=tk.Label(root,text="   ")
label3.grid(row=5)
tk.Button(root, 
          text='Quit', 
          command=root.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(root,text='Add', command=add).grid(row=3, column=1, sticky=tk.W,pady=4)
tk.Button(root,text='Subtraction', command=sub).grid(row=3, column=2, sticky=tk.W,pady=4)
tk.Button(root,text='Product', command=mul).grid(row=3, column=3, sticky=tk.W,pady=4)
tk.Button(root,text='Division', command=div).grid(row=4, column=0, sticky=tk.W,pady=4)
tk.Button(root,text='Floor Division', command=fdiv).grid(row=4, column=1, sticky=tk.W,pady=4)
tk.Button(root,text='Power', command=exp).grid(row=4, column=2, sticky=tk.W,pady=4)

tk.mainloop()