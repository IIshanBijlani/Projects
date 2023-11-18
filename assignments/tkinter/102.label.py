from tkinter import *   #import the tkinter module

def main():
	root = Tk() 		#Create an empty window
	#additional code will come here 
	hello = Label(root, text="Hello world!",fg="yellow",bg="black")
	hello.pack()
	root.mainloop()	#Pause the code and do nothing  
					#until the window is closed
main()
