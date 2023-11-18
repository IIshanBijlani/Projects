import tkinter as tk

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    #e1.delete(2, 4)
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

root = tk.Tk()
tk.Label(root, text="First Name").grid(row=0)
tk.Label(root, text="Last Name").grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.insert(10, "Miller")
e2.insert(10, "Jill")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(root, 
          text='Quit', 
          command=quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(root, text='Show', command=show_entry_fields).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)

root.mainloop()

tk.mainloop()
