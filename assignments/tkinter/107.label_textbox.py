import tkinter as tk

root = tk.Tk()
#tk.Label(root, text="First Name").grid(row=0)
#tk.Label(root, text="Last Name").grid(row=1)

l1=tk.Label(root, text="First Name")
l2=tk.Label(root, text="Last Name")
l1.grid(row=0)
l2.grid(row=1)

#Textbox - Entry
e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

root.mainloop()