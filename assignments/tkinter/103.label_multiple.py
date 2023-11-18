from tkinter import *   #import the tkinter module

def main():
    root = Tk() 		#Create an empty window
	#additional code will come here 
    a_label1 = Label(root, text = "One")
    a_label2 = Label(root, text = "Two")
    a_label3 = Label(root, text = "Three")
	
    
    a_label1.pack()
    a_label2.pack()
    a_label3.pack()
    root.mainloop()	#Pause the code and do nothing  
					#until the window is closed
main()
