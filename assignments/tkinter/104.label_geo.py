from tkinter import *   #import the tkinter module

def main():
    root = Tk() 		#Create an empty window
	#additional code will come here 
    root.geometry("500x300")
    a_label = Label(root, text='Alpha')
    a_label.grid(row=0, column=0)

    b_label = Label(root, text='Beta')
    b_label.grid(row=0, column=2)	

    c_label = Label(root, text='Gamma')
    c_label.grid(row=1, column=1)	
	#no pack, grid is used to position the widgets 
    
    root.mainloop()	#Pause the code and do nothing  
					#until the window is closed
                    
    
main()
