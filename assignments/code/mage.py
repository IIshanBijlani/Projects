from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import random,math,os
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="world"
)
cur=con.cursor()


class campion:
    def __init__(self,root):
        self.root=root
        self.root.title(" School Management")
        self.root.geometry("1350x750+0+0")
        self.color="darkslateblue"
        ##labeltop  school
        self.lbltop=Label(self.root,text="Carmel Convent Senior Secondary Bhopal",bg=self.color,fg="white",font=('Times new roman',40,'bold'),bd=10,relief=GROOVE,)
        self.lbltop.place(x=0,y=0,relwidth=1)

        ####variables
        self.sch_no=IntVar()
        self.Class=StringVar()
        self.Rollno=IntVar()
        self.Name=StringVar()
        self.maths=IntVar()
        self.chemistry=IntVar()
        self.physics=IntVar()
        self.english=IntVar()
        self.optionalmarks=IntVar()
        self.percentage=IntVar()
        self.total=IntVar()
        self.search_var=StringVar()
        self.comboinput=StringVar()
        self.optionalsub=StringVar()
        self.marksheet_data=StringVar()
        #self.contact=IntVar()
        ##variable get 

        ##TOP frame,images  and entries
        frame1=LabelFrame(self.root,bg="black")
        frame1.place(x=0,y=80,width=1350,height=190)
        
        self.infolbl=Label(self.root,text="STUDENT MANAGEMENT SYSTEM:\nStore Record , Generate Marksheet, Delete Record, Update Records ",bg=self.color,fg="magenta",font=('Times new roman',15,'bold'))
        self.infolbl.place(x=280,y=85,width=780,height=80)

        
        #Side campion images
        self.bg1=ImageTk.PhotoImage(file="Tkinterschool.jpg")
        bg1=Label(self.root,image=self.bg1).place(x=0,y=85)
        self.bg2=ImageTk.PhotoImage(file="Tkinterschool.jpg")
        bg2=Label(self.root,image=self.bg2).place(x=1060,y=85)
        #self.bg3=ImageTk.PhotoImage(file="campionheading.jpg")
        #bg3=Label(self.infolbl,image=self.bg3,width=400,height=200).place(x=0,y=10)
        

        
            
        #####Enter detail widgets
        info_frame=LabelFrame(self.root,text='Enter Details',bg=self.color)
        info_frame.place(x=290,y=170,width=770,height=100)

        empty=[]
        x=random.randint(1000,3000)
        
        sch_lbl=Label(info_frame,text="ScholarNo",font=('times new roman',16,'bold'),bg=self.color,fg='limegreen').place(x=10,y=10)
        sch_txt=Entry(info_frame,width=13,textvariable=self.sch_no,font=("times new roman",15,"bold")).place(x=10,y=35)
        if x not in empty:
            self.sch_no.set(str(x))
            empty.append(x)
        class_lbl=Label(info_frame,text="Class",font=("times new roman",16,"bold"),bg=self.color,fg='limegreen').place(x=200,y=10)
        class_txt=ttk.Combobox(info_frame,width=11,textvariable=self.Class,font=("times new roman",15,"bold"))
        class_txt["values"]=('XIA','XIB','XIC','XIIA','XIIB','XIIC')
        class_txt.place(x=200,y=35)
        

        Rollno_lbl=Label(info_frame,text="Rollno",font=("times new roman",16,"bold"),bg=self.color,fg='limegreen').place(x=400,y=10)
        Rollno_txt=Entry(info_frame,width=13,textvariable=self.Rollno,font=("times new roman",15,"bold")).place(x=400,y=35)

        
        Name_lbl=Label(info_frame,text="Name",font=('times new roman',16,'bold'),bg=self.color,fg='limegreen').place(x=590,y=10)
        Name_txt=Entry(info_frame,width=13,textvariable=self.Name,font=("times new roman",15,"bold")).place(x=590,y=35)

        
        #####Marks Frame#####
        marks_frame=LabelFrame(self.root,bg=self.color,bd=10,relief=GROOVE)
        marks_frame.place(x=0,y=270,width=210,height=480)
        maths_lbl=Label(marks_frame,text="Maths",font=('times new roman',18,'bold'),bg=self.color,fg='limegreen')
        maths_lbl.place(x=10,y=20)
        self.maths_txt=Entry(marks_frame,width=20,textvariable=self.maths,bd=5,relief=GROOVE,font=("times new roman",10,"bold"))
        self.maths_txt.place(x=30,y=50)
        
        chemistry_lbl=Label(marks_frame,text="Chemistry",font=('times new roman',18,'bold'),bg=self.color,fg='limegreen')
        chemistry_lbl.place(x=10,y=90)
        chemistry_txt=Entry(marks_frame,width=20,textvariable=self.chemistry,bd=5,relief=GROOVE,font=("times new roman",10,"bold"))
        chemistry_txt.place(x=30,y=120)
        
        physics_lbl=Label(marks_frame,text="Physics",font=('times new roman',18,'bold'),bg=self.color,fg='limegreen')
        physics_lbl.place(x=10,y=160)
        physics_txt=Entry(marks_frame,width=20,textvariable=self.physics,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        physics_txt.place(x=30,y=190)
        
        english_lbl=Label(marks_frame,text="English",font=('times new roman',18,'bold'),bg=self.color,fg='limegreen')
        english_lbl.place(x=10,y=230)
        self.english_txt=Entry(marks_frame,width=20,textvariable=self.english,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        self.english_txt.place(x=30,y=260)
        
        optional_lbl=Label(marks_frame,text="Optional",font=('times new roman',18,'bold'),bg=self.color,fg='limegreen')
        optional_lbl.place(x=10,y=300)
        self.optional_txt=ttk.Combobox(marks_frame,width=18,textvariable=self.optionalsub,font=("times new roman",10,"bold"))
        self.optional_txt['values']=(" ",'Computer','PhysicalEdu','Hindi')
        self.optional_txt.place(x=30,y=330)
        self.optionalmarks_txt=Entry(marks_frame,width=20,textvariable=self.optionalmarks,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        self.optionalmarks_txt.place(x=30,y=360)
       
        
        
        
        
        
        
        Middlelbl=Label(self.root,bg=self.color,bd=10,relief=GROOVE)
        Middlelbl.place(x=210,y=270,width=1140,height=70)
        
        searchby_lbl=Label(Middlelbl,text="To find any record hit : Search by:",font=('times new roman',18,'bold'),bg=self.color,fg='limegreen')
        searchby_lbl.place(x=280,y=10)
        self.searchselect_txt=ttk.Combobox(Middlelbl,width=18,font=("times new roman",10,"bold"),textvariable=self.comboinput)
        self.searchselect_txt['values']=(" ",'ScholarNo','Name' ,'Class')
        self.searchselect_txt.place(x=640,y=15)
        self.searchentry=Entry(Middlelbl,width=15,textvariable=self.search_var,font=("times new roman",13,"bold"),bd=5)
        self.searchentry.place(x=810,y=12)
        Btn_searchrecord=Button(Middlelbl,text='Search',width=13,bd=5,font=('arial',10,'bold'),bg="Green",fg='white',command=lambda:self.Search_record()).place(x=980,y=12)
        
        
        

        ###bottom button frame
        bottomframe=Frame(self.root,bg=self.color,bd=10,relief=GROOVE)
        bottomframe.place(x=210,y=640,width=1140,height=110)
        Btn_Fetchdata=Button(bottomframe,text='Fetch Data',command=lambda:self.fetch_data(),font=('arial',12,'bold'),bd=10,width=10,height=3,bg="Green",fg='white').grid(row=0,column=0,padx=13,pady=5)
        Btn_StoreResult=Button(bottomframe,text='Store \nResult',width=10,bd=10,height=3,font=('arial',12,'bold'),bg="Green",fg='white',command=lambda:self.add_student()).grid(row=0,column=1,padx=13,pady=5)
        Btn_generatemarksheet=Button(bottomframe,text='Generate \nMarksheet',width=10,bd=10,height=3,bg="Green",font=('arial',12,'bold'),fg='white',command=lambda:self.generatemarksheet()).grid(row=0,column=2,padx=13,pady=5)
        Btn_update=Button(bottomframe,text='Update',font=('arial',12,'bold'),bd=10,width=10,height=3,bg="Green",fg='white',command=lambda:self.update_data()).grid(row=0,column=3,padx=13,pady=5)
        Btn_delete=Button(bottomframe,text='Delete',font=('arial',12,'bold'),bd=10,width=10,height=3,bg="Green",fg='white',command=lambda:self.delete_data()).grid(row=0,column=4,padx=13,pady=5)
        Btn_clear=Button(bottomframe,text='Clear',width=10,bd=10,height=3,bg="Green",font=('arial',12,'bold'),fg='white',command=lambda:self.clear()).grid(row=0,column=5,padx=13,pady=5,)
        Btn_exit=Button(bottomframe,text='Exit',font=('arial',12,'bold'),bd=10,width=10,height=3,bg="Green",fg='white',command=lambda:self.exitbutton()).grid(row=0,column=6,padx=13,pady=5)
        
        #####Table frame
        Table_frame=LabelFrame(self.root,bd=10,relief=GROOVE,bg="gray")
        Table_frame.place(x=210,y=340,width=1150,height=300)
        
        style=ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("mystyle.Treeview",highlightthickness=20,bd=20,font=('Calibri',11,'bold'),background="pink",foreground="blue")
        
        style.configure("mystyle.Treeview.Heading",font=('Calibri',13,'bold'),background="cyan")
        style.layout("mystyle.Treeview",[('mystyle.Treeview.treearea',{'sticky':'nswe'})])
        

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,style="mystyle.Treeview",columns=("ScholarNo","Class","Rollno","Name","Maths","Chemistry","Physics","English","Optional","Total","Percentage"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #self.student_table.configure("mystyle.Treeview",style="mystyle.Treeview")

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("ScholarNo",text="ScholarNo")
        self.student_table.heading("Class",text="Class")
        self.student_table.heading("Rollno",text="Rollno")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Maths",text="Maths")
        self.student_table.heading("Chemistry",text="Chemistry")
        self.student_table.heading("Physics",text="Physics")
        self.student_table.heading("English",text="English")
        self.student_table.heading("Optional",text="Optional")
        self.student_table.heading("Percentage",text="Percentage")
        self.student_table.heading("Total",text="Total")
        self.student_table['show']='headings'
        self.student_table.column("ScholarNo",width=100)
        self.student_table.column("Class",width=100)
        self.student_table.column("Rollno",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Maths",width=100)
        self.student_table.column("Chemistry",width=100)
        self.student_table.column("Physics",width=100)
        self.student_table.column("English",width=100)
        self.student_table.column("Optional",width=100)
        self.student_table.column("Percentage",width=100)
        self.student_table.column("Total",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
    ####functions
    def generatemarksheet(self):
        Txt_frame=LabelFrame(self.root,bd=10,relief=GROOVE,bg="gray")
        Txt_frame.place(x=210,y=340,width=1150,height=300)
        scrol_y=Scrollbar(Txt_frame,orient=VERTICAL)
        self.txtarea=Text(Txt_frame,font=('arial',12,'bold'),yscrollcommand=scrol_y.set)
        self.txtarea.configure(background="orchid")
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.configure(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH)

        self.total=self.maths.get()+self.chemistry.get()+self.physics.get()+self.english.get()+self.optionalmarks.get()
        self.percentage=self.total/5
        #self.txtarea.insert(END,"\n  ")
        self.txtarea.insert(END,"\t\t\t=============CAMPION SCHOOL BHOPAL============")
        self.txtarea.insert(END,"\n\t\t\t=========FIRST TERMINAL EXAMINATION 2020========")
        self.txtarea.insert(END,"\n  ")
        self.txtarea.insert(END,f"\n \t\t\t    Scholar No:{self.sch_no.get()}\t\t\t Class:{self.Class.get()}")
        self.txtarea.insert(END,f"\n \t\t\t    Name:{self.Name.get()}\t\t\t  RollNO:{self.Rollno.get()}")
        
        self.txtarea.insert(END,f"\n \t\t\t---------------------------------------------------------------------------------------")
        self.txtarea.insert(END,f"\n \t\t\t    Maths:\t{self.maths.get()}")
        self.txtarea.insert(END,f"\n \t\t\t    Chemistry:\t{self.chemistry.get()}")
        self.txtarea.insert(END,f"\n \t\t\t    Physics:\t{self.physics.get()}")
        self.txtarea.insert(END,f"\n \t\t\t    English:\t{self.english.get()}")
        self.txtarea.insert(END,f"\n \t\t\t    Additonal:\t{self.optionalmarks.get()}")
        #self.txtarea.insert(END,"\n  ")
        self.txtarea.insert(END,f"\n \t\t\t===================================================")
        self.txtarea.insert(END,f"\n \t\t\t    Total:{self.total}\t\t\tPercentage:{self.percentage}%")
        
        self.txtarea.insert(END,f"\n \t\t\t===================================================")
        self.printmarksheet()
        
    def printmarksheet(self):
        op=messagebox.askyesno("Print","Do you want to print Marksheet" )
        if op>0:
            self.marksheet_data=self.txtarea.get("1.0",END)
            f1=open("marksheet/"+str(self.sch_no.get())+".txt","w")
            f1.write(self.marksheet_data)       
            f1.close()
            messagebox.showinfo("Saved",f"Student no.{self.sch_no.get()}has been saved successfully")
        else:
            return
     
                              
                              
                              
                              
                              
        
    def exitbutton(self):
        root.destroy()
            
        
        
    def clear(self):
        #self.sch_no.set("")
        self.Class.set("")
        self.Rollno.set("")
        self.Name.set("")
        self.maths.set(0)
        self.chemistry.set(0)
        self.physics.set(0)
        self.english.set(0)
        self.optionalmarks.set(0)
        self.student_table.delete(*self.student_table.get_children())
        self.txtarea.delete('1.0',END)
           
    def add_student(self):    
        self.total=self.maths.get()+self.chemistry.get()+self.physics.get()+self.english.get()+self.optionalmarks.get()
        self.percentage=self.total/5
        con=mysql.connector.connect(host='localhost',user='root',password='mysql',database='world')
        cur=con.cursor()
        if self.Class.get()=="" or self.Rollno.get()==0 or self.Name.get()=="" :
                        messagebox.showerror('Error',"Student Detail Class,Name,Rollno is must " )
        else:       
            cur.execute("insert into campionresult(ScholarNo,Class,Rollno,Name,Maths,Chemistry,Physics,English,Optional,Total,Percentage)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                                %(self.sch_no.get(),
                                self.Class.get(),
                                self.Rollno.get(),
                                self.Name.get(),
                                self.maths.get(),
                                self.chemistry.get(),
                                self.physics.get(),
                                self.english_txt.get(),
                                self.optionalmarks.get(),
                                self.total,
                                self.percentage))          
            con.commit() 
            messagebox.showinfo('Congrats',"Record has been saved in Database ,U may Fetch record " )
   
        #self.fetch_data()
        #self.clear()
        
        con.close()
    def fetch_data(self):
        Table_frame=LabelFrame(self.root,bd=10,relief=GROOVE,bg="gray")
        Table_frame.place(x=210,y=340,width=1150,height=300)

        style=ttk.Style(self.root)
        style.theme_use("clam")
        
        style.configure("mystyle.Treeview",highlightthickness=0,bd=0,font=('Calibri',11,'bold'))
        style.configure("mystyle.Treeview.Heading",font=('Calibri',13,'bold'),background="cyan")
        style.layout("mystyle.Treeview",[('mystyle.Treeview.treearea',{'sticky':'nswe'})])
        #tree.tag_configure(background='pink')
        
        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,style="mystyle.Treeview",columns=("ScholarNo","Class","Rollno","Name","Maths","Chemistry","Physics","English","Optional","Total","Percentage"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("ScholarNo",text="ScholarNo")
        self.student_table.heading("Class",text="Class")
        self.student_table.heading("Rollno",text="Rollno")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Maths",text="Maths")
        self.student_table.heading("Chemistry",text="Chemistry")
        self.student_table.heading("Physics",text="Physics")
        self.student_table.heading("English",text="English")
        self.student_table.heading("Optional",text="Optional")
        self.student_table.heading("Percentage",text="Percentage")
        self.student_table.heading("Total",text="Total")
        self.student_table['show']='headings'
        self.student_table.column("ScholarNo",width=100)
        self.student_table.column("Class",width=100)
        self.student_table.column("Rollno",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Maths",width=100)
        self.student_table.column("Chemistry",width=100)
        self.student_table.column("Physics",width=100)
        self.student_table.column("English",width=100)
        self.student_table.column("Optional",width=100)
        self.student_table.column("Percentage",width=100)
        self.student_table.column("Total",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        con=mysql.connector.connect(host='localhost',user='root',password='mysql',database='world')
        cur=con.cursor()

        cur.execute("select * from campionresult")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.sch_no.set(row[0])
        self.Class.set(row[1])
        self.Rollno.set(row[2])
        self.Name.set(row[3])
        self.maths.set(row[4])
        self.chemistry.set(row[5])
        self.physics.set(row[6])
        self.english.set(row[7])
        self.optionalmarks.set(row[8])
        
    def Search_record(self):
        con=mysql.connector.connect(host='localhost',user='root',password='mysql',database='world')
        cur=con.cursor()
        self.student_table.delete(*self.student_table.get_children())
            
        str1=self.comboinput.get()
        if (str1=='ScholarNo'):
            
            cur.execute("select * from campionresult where ScholarNo='%s' "%(self.search_var.get()))
            row=cur.fetchone()
            if row!=None:
                self.student_table.insert('',END,values=row)
            else:
                messagebox.showerror('Error',"No such record found")
        elif (str1=='Name'):         
            cur.execute("select * from campionresult where Name='%s' "%(self.search_var.get()))
            row=cur.fetchone()
            if row!=None:
                self.student_table.insert('',END,values=row)
            else: 
                messagebox.showerror('Error',"No such record found")
        elif (str1=='Class'):
            cur.execute("select * from campionresult" )
            rows=cur.fetchall()
            
            count=0
            for row in rows:
                if row[1]==self.search_var.get():
                    self.student_table.insert('',END,values=row)
                    count=1
            if count==0:
                messagebox.showerror('Error',"No such record found")
                    
        con.commit()
        con.close() 
       


    def update_data(self):
        self.total=self.maths.get()+self.chemistry.get()+self.physics.get()+self.english.get()+self.optionalmarks.get()
        self.percentage=self.total/5
       
        con=mysql.connector.connect(host='localhost',user='root',password='mysql',database='world')
        cur=con.cursor()
        cur.execute("update campionresult set Class='%s',Rollno='%s',Name='%s',Maths='%s',Chemistry='%s',Physics='%s',English='%s',Optional='%s',Total='%s',Percentage='%s'  where ScholarNo= '%s' "
                                                                                                                                       %( self.Class.get(),
                                                                                                                                        self.Rollno.get(),
                                                                                                                                        self.Name.get(),
                                                                                                                                        self.maths.get(),
                                                                                                                                        self.chemistry.get(),
                                                                                                                                        self.physics.get(),
                                                                                                                                        self.english_txt.get(),
                                                                                                                                        self.optionalmarks.get(),
                                                                                                                                        self.total,
                                                                                                                                        self.percentage,
                                                                                                                                        self.sch_no.get()
                                                                                                                                        ))
                                                                                                                
        con.commit()                                                                                                    
        self.fetch_data()
        #self.clear()
        con.close()    
                
    def delete_data(self):
        con=mysql.connector.connect(host='localhost',user='root',password='mysql',database='world')
        cur=con.cursor()

        cur.execute("delete from campionresult where ScholarNo='%s' "%self.sch_no.get())
        con.commit()
        self.fetch_data()
        con.close()
        

            
            
        
root=Tk()                 
obj=campion(root)
root.mainloop()
