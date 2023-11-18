

from tkinter import *
cal=Tk()
cal.title("Calculator")
operator=" "

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
text_input=StringVar()

def btncleardisplay():
    global operator
    operator=" "
    text_input.set(" ")
def btnequalinput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=" "
txtdisplay=Entry(cal,font=('arial',16,'bold'),textvariable=text_input,bd=30,insertwidth=6,bg="powderblue", justify='right').grid(columnspan=4)


btn7=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:btnclick("7")).grid(row=2,column=0)
btn8=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:btnclick("8")).grid(row=2,column=1)
btn9=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:btnclick("9")).grid(row=2,column=2)
Addition=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=2,column=3)

btn4=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:btnclick("4")).grid(row=3,column=0)
btn5=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:btnclick("5")).grid(row=3,column=1)
btn6=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:btnclick("6")).grid(row=3,column=2)
minus=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=3,column=3)

btn1=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:btnclick("1")).grid(row=4,column=0)
btn2=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:btnclick("2")).grid(row=4,column=1)
btn3=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:btnclick("3")).grid(row=4,column=2)
multiply=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda:btnclick("*")).grid(row=4,column=3)

btn0=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:btnclick("0")).grid(row=5,column=0)
btnclear=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",command=lambda:btncleardisplay()).grid(row=5,column=1)
btnequal=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=lambda:btnequalinput()).grid(row=5,column=2)
division=Button(cal,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:btnclick("/")).grid(row=5,column=3)



cal.mainloop()