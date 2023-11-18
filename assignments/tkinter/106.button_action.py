from tkinter import *
def main():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    button = Button(frame,text="QUIT", fg="red",command=quit)
    button.pack(side=LEFT)
    slogan = Button(frame,text="Hello",command=write_slogan)
    slogan.pack(side=LEFT)
    root.mainloop()

def write_slogan():
    print("Tkinter is easy to use!")

main()