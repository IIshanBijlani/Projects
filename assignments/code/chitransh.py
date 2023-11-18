from tkinter import * 

root = Tk()

frame =Frame(root, width=300,height=230)
button1 = Button(frame, text="button1")
button2 = Button(frame, text="button2")
button3 = Button(frame, text="button3")
button4 = Button(frame, text="button4")
button5 = Button(frame, text="button5")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
frame.pack()

bottomFrame = Frame(root)

button6 = Button(bottomFrame, text="ok ")
button6.pack
root.mainloop()