import tkinter as tk

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
	
def show_entry_fields2():
    a="Welcome : "+e1.get()+" "+e2.get()
    label3.config(text=a)
    
def change_entry_fields():
    label1.config(text="Hello world")


root = tk.Tk()
root.configure(background='pink')
label1=tk.Label(root, 
         text="First Name")
label1.grid(row=0)
label2=tk.Label(root, 
         text="Last Name")
label2.grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#this line gives error if we create a label and show it in a single statement
#label3=tk.Label(root,text="   ").grid(row=5)
label3=tk.Label(root,text="   ")
label3.grid(row=5)
tk.Button(root, 
          text='Quit', 
          command=root.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(root, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
tk.Button(root, 
          text='Show2', command=show_entry_fields2).grid(row=3, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.Button(root, 
          text='change', command=change_entry_fields).grid(row=3, 
                                                       column=3, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()