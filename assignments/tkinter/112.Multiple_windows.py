#import module needed
import tkinter as tk
#write the new window function which
#will be called when button pressed
def new_window():
    window = tk.Toplevel(root).title("Child window")
    

#create original window 
root = tk.Tk()
root.title("My Window ")
root.geometry("400x300")
#create button that will be placed
button = tk.Button(root, text="new window", bg='black', fg='#ff0000',
                              command=new_window)

button.pack()
root.mainloop()
