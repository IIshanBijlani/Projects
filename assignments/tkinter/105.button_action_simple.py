from tkinter import *   #import the tkinter module

def main():
	root = Tk() 		#Create an empty window
	#additional code will come here 
	button = Button(text="QUIT", fg="red",command=quit)
	button.pack()
	slogan = Button(text="Hello",command=write_slogan)
	slogan.pack()
	root.mainloop()	#Pause the code and do nothing  
					#until the window is closed

def write_slogan():
    print("Tkinter is easy to use!")

main()
