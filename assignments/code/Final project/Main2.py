# smiriti maam error

# result creator

# Final code for now

import tkinter as tk
import os
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas
import shutil
from PIL import ImageTk


# Functions to make widgets in tkinter=================================================================================
def label(frame, text, font, bg, fg, r, c, x, y):
    l = tk.Label(frame, text=text, font=f"lucidia {font} bold", bg=bg, fg=fg).grid(row=r, column=c, padx=x, pady=y)
    return l


def button(frame, text, font, bg, fg, r, c, x, y, command):
    b = tk.Button(frame, text=text, font=f"lucidia {font} bold", bg=bg, fg=fg, command=command).grid(row=r, column=c,
                                                                                                     padx=x, pady=y)
    return b


# Frames of all the forms and windows===================================================================================
def dataCreater_form():
    global tc, f2, tp
    f2 = tk.Frame(root)
    f2.place(x=0, y=0, width=800, height=500)

    pic_label1 = tk.Label(f2, image=pic1).place(x=0, y=0, relheight=1, relwidth=1)

    label(f2, "Add Name of Data", 15, "light blue", None, 0, 0, 190, 30)
    tc = tk.Entry(f2, font="lucidia 15 bold", width=25)
    tc.grid(row=1, column=0, padx=210, pady=5)
    tk.Button(f2, text="Continue", font='lucidia 15 bold', bg="light blue",
              command=continue_datacreate).place(x=300, y=140)

    tk.Label(f2, text='Add Path of CSV file', font='lucidia 15 bold', bg='light blue').place(x=270, y=250)
    tp = tk.Entry(f2, font="lucidia 15 bold", width=50)
    tp.place(x=100, y=300)
    tk.Button(f2, text="Import", font='lucidia 15 bold', bg="light blue",
              command=importer).place(x=300, y=330)

    tk.Button(f2, text="Back", font='lucidia 15 bold', bg="light blue",
              command=f2.destroy).place(x=300, y=450)
    tk.Button(f2, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\second form.png')).place(x=720, y=5)


def dataRemover_form():
    global tr, f3
    f3 = tk.Frame(root)
    f3.place(x=0, y=0, width=800, height=500)
    pic_label2 = tk.Label(f3, image=pic2).place(x=0, y=0, relheight=1, relwidth=1)
    label(f3, "Add Name of Data To Remove It", 30, None, None, 0, 0, 100, 50)
    tr = tk.Entry(f3, font="lucidia 30 bold")
    tr.grid(row=1, column=0, padx=100, pady=25)
    button(f3, "Continue", 30, "blue", None, 2, 0, 100, 25, continue_dataRemover)
    button(f3, "Back", 30, "yellow", None, 3, 0, 10, 25, f3.destroy)
    tk.Button(f3, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\download.png')).place(x=750, y=5)


def importer():
    path = tp.get()
    spliter = list(path.split('\\'))
    lst_name = list(spliter[-1].split('.'))
    dataname = lst_name[0]

    # Create folder name of csv
    try:
        os.mkdir(f'Data\\{dataname}')
    except:
        messagebox.showerror('Already existed csv name please type continue instead of import')
        dataCreater_form()

    df = pandas.read_csv(path, index_col=0)
    print(df)
    lst_student = list(df.index)
    print(lst_student)
    x = 0
    # Create folder of students
    for i in lst_student:
        os.mkdir(f'Data\\{dataname}\\{i}')

        f = open(f'Data\\{dataname}\\{i}\\marks.txt', 'x')
        marks_lst = list(df.iloc[x])
        f.write(f'{marks_lst[0]},{marks_lst[1]},{marks_lst[2]},{marks_lst[3]},{marks_lst[4]}')

        add = marks_lst[0] + marks_lst[1] + marks_lst[2] + marks_lst[3] + marks_lst[4]
        perc = round((add/500)*100, 2)
        grade = grade_calculator(perc)

        f2 = open(f'Data\\{dataname}\\{i}\\grade.txt', 'x')
        grade_lst = f"{add},{perc},{grade},{marks_lst[5]},{marks_lst[6]}"
        f2.write(grade_lst)
        f.close()
        f2.close()

        x = x + 1

    done_entryform()


def continue_datacreate():
    # Backend code:
    try:
        # Appearance code
        text = tc.get()
        if text == "":
            messagebox.showwarning("Warning", "Please Fill Name then Proceed")
            cont_fr.destroy()
        else:
            os.mkdir(f"Data\\{tc.get()}")
            messagebox.showinfo("Successful", f"Data '{tc.get()}' has been created successfully")

            continue_datacreate2()

    except:
        messagebox.showinfo("Attention", "Similar Name Database exists already, you will be continuing ")
        continue_datacreate2()


def continue_datacreate2():
    global name, addmision, mat, soc, eng, hin, sci, gen, cont_fr
    cont_fr = tk.Frame(root)
    cont_fr.place(x=0, y=0, width=800, height=500)
    pic_label1 = tk.Label(cont_fr, image=pic6).place(x=0, y=0, relheight=1, relwidth=1)
    # Labels
    tk.Label(cont_fr, text="Name", font="lucidia 25 bold").place(x=1, y=4)
    tk.Label(cont_fr, text="Admission", font="lucidia 20 bold").place(x=1, y=52)
    tk.Label(cont_fr, text="Maths", font="lucidia 15 bold").place(x=30, y=140)
    tk.Label(cont_fr, text="Physics", font="lucidia 15 bold").place(x=30, y=170)
    tk.Label(cont_fr, text="Chemistry", font="lucidia 15 bold").place(x=30, y=200)
    tk.Label(cont_fr, text="English", font="lucidia 15 bold").place(x=30, y=230)
    tk.Label(cont_fr, text="Optional", font="lucidia 15 bold").place(x=30, y=260)
    tk.Label(cont_fr, text="Gender", font="lucidia 20 bold").place(x=500, y=150)

    # Entries
    name = tk.Entry(cont_fr, font="lucidia 20 bold")
    name.place(x=170, y=4)
    addmision = tk.Entry(cont_fr, font="lucidia 20 bold")
    addmision.place(x=170, y=51)
    mat = tk.Entry(cont_fr, font="lucidia 15 bold")
    mat.place(x=130, y=140)
    sci = tk.Entry(cont_fr, font="lucidia 15 bold")
    sci.place(x=130, y=170)
    eng = tk.Entry(cont_fr, font="lucidia 15 bold")
    eng.place(x=130, y=200)
    hin = tk.Entry(cont_fr, font="lucidia 15 bold")
    hin.place(x=130, y=230)
    soc = tk.Entry(cont_fr, font="lucidia 15 bold")
    soc.place(x=130, y=260)
    gen = tk.Entry(cont_fr, font="lucidia 15 bold")
    gen.place(x=500, y=190)

    # Buttons
    tk.Button(cont_fr, text="Save and Next", font="lucidia 30 bold", bg="light green", command=next_entryform).place(
        x=60,
        y=350)
    tk.Button(cont_fr, text="Show", font="lucidia 30 bold", bg="light green", command=show_entryform).place(x=410,
                                                                                                            y=350)
    tk.Button(cont_fr, text="Done", font="lucidia 30 bold", bg="light green", command=done_entryform).place(x=610,
                                                                                                            y=350)

    tk.Button(cont_fr, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\entry form.png')).place(x=750, y=5)


def next_entryform():
    try:
        student_name = name.get()
        addmission_no = addmision.get()
        english = float(eng.get())
        hindi = float(hin.get())
        maths = float(mat.get())
        science = float(sci.get())
        sst = float(soc.get())
        report = tc.get()
        gender = gen.get()

        # Making folder by name of student and txt file for marks
        os.mkdir(f"Data\\{report}\\{student_name}")
        f = open(f"Data\\{report}\\{student_name}\\marks.txt", "x")
        stri = f"{maths},{science},{sst},{english},{hindi}"
        f.write(stri)
        f.close()

        # Making a txt file for grades
        total_marks = (maths + science + sst + english + hindi)
        percentage = round(((total_marks / 500) * 100), 2)
        grade_provided = grade_calculator(percentage)
        fg = open(f"Data\\{report}\\{student_name}\\grade.txt", "x")
        strig = f"{total_marks},{percentage},{grade_provided}, {gender}, {addmission_no}"
        fg.write(strig)
        fg.close()

        # Graph Resources
        index_list = ['Maths', 'Physics', 'Chemistry', 'English', 'Optional']
        marks_list = [maths, science, sst, english, hindi]
        clrs = ["#2E2EFE", "#FF0040", "#F7FE2E", "#40FF00", "#FF8000"]

        # Graph converter
        line_chart(index_list, marks_list, student_name, report)
        bar_chart(index_list, marks_list, student_name, report)

        # plt.legend(loc='upper left')
        # plt.title(f"{student_name} Marks")
        plt.xlabel('subjects')
        plt.ylabel('Marks')
        # plt.savefig(f"Data\\{report}\\{student_name}\\{student_name} Marks Graph.png")

        name.delete(0, 'end')
        addmision.delete(0, 'end')
        mat.delete(0, 'end')
        sci.delete(0, 'end')
        soc.delete(0, 'end')
        hin.delete(0, 'end')
        eng.delete(0, 'end')

        messagebox.showinfo("Success", f"Created Data For {student_name} Successfully")

        cont_fr.mainloop()
    except:
        name.delete(0, 'end')
        addmision.delete(0, 'end')
        mat.delete(0, 'end')
        sci.delete(0, 'end')
        soc.delete(0, 'end')
        hin.delete(0, 'end')
        eng.delete(0, 'end')

        messagebox.showerror("Error", "Please type only numerical digits for marks boxes")

        cont_fr.mainloop()


def done_entryform():
    global done_fr
    database_name = tc.get()
    done_fr = tk.Frame(root)
    done_fr.place(x=0, y=0, width=800, height=500)
    pic_label1 = tk.Label(done_fr, image=pic10).place(x=0, y=0, relheight=1, relwidth=1)
    tk.Label(done_fr, text=f"Successfully Created \n({database_name}) Database", font="lucidia 25 bold").place(x=250,
                                                                                                             y=30)

    # Buttons
    tk.Button(done_fr, text="Arranged \nData", font="lucidia 30 bold", bg="light blue", command=arranged_data).place(
        x=110,
        y=150)
    tk.Button(done_fr, text="Export to \nMS Excel", font="lucidia 30 bold", bg="light green",
              command=export_excelform).place(x=410, y=150)
    tk.Button(done_fr, text="Show each\n Student", font="lucidia 30 bold", bg="pink", command=show_each_student).place(
        x=110, y=300)

    tk.Button(done_fr, text="Create New\n Report", font="lucidia 30 bold", bg="yellow", command=dataCreater_form).place(
        x=410, y=300)
    tk.Button(done_fr, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\main functions.png')).place(x=750, y=5)


def show_entryform():
    global show_frame
    data_name = tc.get()
    show_frame = tk.Frame()
    show_frame.place(x=0, y=0, width=800, height=500)
    pic_label2 = tk.Label(show_frame, image=pic7).place(x=0, y=0, relheight=1, relwidth=1)

    box = tk.Text(show_frame, font="lucidia 25 bold", width=150, height=10)
    box.place(x=0, y=50)

    label_hd(show_frame, 'All Students Saved till now', 27, None, 190, 0)
    tk.Button(show_frame, text='Back', font='lucidia 25 bold', bg='orange', command=show_frame.destroy).place(
        x=315, y=435)
    tk.Button(show_frame, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\download.png')).place(x=750, y=5)

    # Name Extractor
    lst = os.listdir(f"Data\\{data_name}")
    lst.sort(reverse=True)
    x = len(lst) + 1
    for i in lst:
        x = x - 1
        box.insert(1.0, f"{x}. {i}\n")

    box.config(state='disabled')


def export_excelform():
    global path_box
    excel_fr = tk.Frame(root)
    excel_fr.place(x=0, y=0, width=800, height=500)
    pic_label3 = tk.Label(excel_fr, image=pic11).place(x=0, y=0, relheight=1, relwidth=1)

    tk.Label(excel_fr, text="Please Enter Path For Saving\n Excel File", font="lucidia 25 bold").place(x=150, y=70)
    path_box = tk.Entry(excel_fr, font="lucidia 20 bold", width=40)
    path_box.place(x=80, y=160)
    tk.Button(excel_fr, text="Create", font="lucidia 30 bold", bg='light green', command=csv_converter).place(x=200,
                                                                                                              y=200)
    tk.Button(excel_fr, text="Back", font="lucidia 30 bold", bg='yellow', command=excel_fr.destroy).place(x=370, y=200)
    tk.Button(excel_fr, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\download.png')).place(x=750, y=5)


def csv_converter():
    try:
        dataname = tc.get()
        path = rf"{path_box.get()}"
        student_names_list = os.listdir(f"Data\\{dataname}")
        dct = {}

        # This loop will convert all name and marks into dictionary
        for name in student_names_list:
            f = open(f"Data\\{dataname}\\{name}\\marks.txt", 'r')
            f2 = open(f"Data\\{dataname}\\{name}\\grade.txt", 'r')
            marks = f"{f.read()},{f2.read()}"
            dct[name] = list(marks.split(","))


        # Above mined data will be converted into dataframe
        Dataframe = pandas.DataFrame(dct, index=['Maths', 'Physics', 'Chemistry', 'English', 'Optional',
                                                 'Total Marks', 'Percentage', 'Grade', 'Gender', 'Admission no.'])
        transposed_df = Dataframe.T
        transposed_df.to_csv(f"{path}\\{dataname}.csv")
        messagebox.showinfo("Success", f"The Database ({dataname}) successfully converted into excel file")
    except:
        path_box.delete(0, 'end')
        messagebox.showerror("Error", 'Specified Path is Incorrect')


def continue_dataRemover():
    try:
        input = tr.get()
        if input == "":
            messagebox.showwarning("Warning", "Please Fill The Name")
        else:
            shutil.rmtree(f"Data\\{input}")
            messagebox.showinfo("Successful", f"Data {input} has been removed from records")
    except:
        messagebox.showerror("Error", "Mentioned Data Doesn't Exsist")
        dataRemover_form()


def continue_dataShow():
    f = tk.Frame(root)
    f.place(x=0, y=0, width=800, height=500)
    pic_label1 = tk.Label(f, image=pic3).place(x=0, y=0, relheight=1, relwidth=1)
    box = tk.Text(f, font="lucidia 25 bold", bg="light blue", width=300, height=10)
    box.place(x=0, y=50)
    tk.Label(f, text="All Databases:", font="lucidia 25 bold", bg="light blue", border=5).place(x=280, y=0)
    tk.Button(f, text="Back", font="lucidia 25 bold", bg="light blue", command=f.destroy).place(x=341, y=434)
    tk.Button(f, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\download.png')).place(x=750, y=5)

    lst = os.listdir("Data")
    lst.sort(reverse=True)
    x = len(lst) + 1
    for i in lst:
        x = x - 1
        box.insert(1.0, f"{x}. {i}\n")

    box.config(state='disabled')


# Calculate Grade of a student
def grade_calculator(percent):
    if 90.01 <= percent <= 100.0:
        return "A1"
    elif 80.01 <= percent <= 90.0:
        return "A2"
    elif 70.01 <= percent <= 80.0:
        return "B1"
    elif 60.01 <= percent <= 70.0:
        return "B2"
    elif 50.01 <= percent <= 60.0:
        return "C1"
    elif 40.01 <= percent <= 50.0:
        return "C2"
    elif 31.0 <= percent <= 40.0:
        return "D"
    else:
        return "You failed"


def line_chart(index_list, marks_list, student_name, report):
    plt.figure(facecolor='black')
    plt.plot(index_list, marks_list, color='yellow', label='range1', marker='d', markerfacecolor="blue")
    plt.legend(loc='upper left')
    ax = plt.axes()
    ax.set_facecolor("#610B21")  # set inbox bg color

    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')  # set xaxis value color
    ax.xaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')

    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')  # set yaxis value color
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='y', colors='white')
    plt.title(f"{student_name} Marks")
    plt.xlabel('subjects')
    plt.ylabel('Marks')
    plt.savefig(f"Data\\{report}\\{student_name}\\{student_name} Marks Line Graph.png")
    plt.close()


def bar_chart(index_list, marks_list, student_name, report):
    plt.figure(facecolor='black')
    plt.bar(index_list, marks_list, width=0.25, label="marks", edgecolor="black",
            color=["blue", "red", "yellow", "green", "#FF8000"])
    ax = plt.axes()
    ax.set_facecolor("#380B61")  # set inbox bg color

    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')  # set xaxis value color
    ax.xaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')

    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')  # set yaxis value color
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='y', colors='white')
    plt.title(f"{student_name} Marks")
    plt.title(f"{student_name} Marks")
    plt.xlabel('subjects')
    plt.ylabel('Marks')
    plt.savefig(f"Data\\{report}\\{student_name}\\{student_name} Marks Bar Graph.png")
    plt.close()


def label_hd(frame1, text1, font, fg, x, y):
    labe = tk.Label(frame1, text=text1, font=f"lucidia {font} bold", fg=fg).place(x=x, y=y)
    return labe


def show_each_student():
    global name_of_student
    name_frame = tk.Frame(root)
    name_frame.place(x=0, y=0, width=800, height=500)
    pic_label1 = tk.Label(name_frame, image=pic4).place(x=0, y=0, relheight=1, relwidth=1)
    tk.Label(name_frame, text='Enter Name of Student', font='lucidia 35 bold').place(x=130, y=60)
    name_of_student = tk.Entry(name_frame, font='lucidia 35 bold')
    name_of_student.place(x=130, y=130)
    tk.Button(name_frame, text="Continue", font='lucidia 35 bold', bg='pink', command=result_form).place(x=130, y=195)
    tk.Button(name_frame, text="Back", font='lucidia 35 bold', bg='pink', command=name_frame.destroy).place(x=380,
                                                                                                            y=195)
    tk.Button(name_frame, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\student.png')).place(x=750, y=5)


def result_form():
    global result_frame, grade_lst
    try:
        result_frame = tk.Frame(root)
        result_frame.place(x=0, y=0, width=800, height=500)
        name = name_of_student.get()
        database = tc.get()

        # Folder of Student Name to list=============================
        f_marks = open(f'Data\\{database}\\{name}\\marks.txt', 'r')
        marks_str = f_marks.read()
        marks_lst = list(marks_str.split(','))

        f_grade = open(f'Data\\{database}\\{name}\\grade.txt', 'r')
        grade_str = f_grade.read()
        grade_lst = list(grade_str.split(','))

        # Rank seprator==============================================
        marks_dct = {}
        ranked_dct = {}
        name_list = os.listdir(f"Data\\{database}")

        # Mining total marks from txt file and getting them in dictionary
        for name1 in name_list:
            f = open(f"Data\\{database}\\{name1}\\grade.txt", "r")
            grade = list(f.read().split(","))
            total_marks = grade[1]
            marks_dct[name1] = total_marks

        # Making a new dictionary with ranked students
        sorted_key = sorted(marks_dct, key=marks_dct.get, reverse=True)
        for i in sorted_key:
            ranked_dct[i] = marks_dct[i]

        res = list(ranked_dct.keys()).index(name)
        rank = int(res) + 1

        # Design output===================================================
        label_hd(result_frame, 'Name', 20, None, 20, 20)
        label_hd(result_frame, 'Addmission', 20, None, 20, 70)
        label_hd(result_frame, 'Gender', 30, None, 380, 20)

        label_hd(result_frame, 'Marks', 30, None, 20, 150)
        label_hd(result_frame, 'Maths', 20, None, 30, 220)
        label_hd(result_frame, 'Physics', 20, None, 30, 250)
        label_hd(result_frame, 'Chemistry', 20, None, 30, 280)
        label_hd(result_frame, 'English', 20, None, 30, 310)
        label_hd(result_frame, 'Optional', 20, None, 30, 340)

        label_hd(result_frame, 'Rank', 30, None, 310, 180)
        label_hd(result_frame, 'Grade', 30, None, 310, 280)
        label_hd(result_frame, 'Percentage', 30, None, 570, 180)
        label_hd(result_frame, 'Total Marks', 30, None, 570, 280)

        # Design Input=====================================================
        label_hd(result_frame, name, 20, 'Blue', 200, 20)
        label_hd(result_frame, grade_lst[-1], 20, 'Blue', 200, 70)
        label_hd(result_frame, grade_lst[-2], 30, 'Blue', 380, 60)

        label_hd(result_frame, marks_lst[0], 20, 'Blue', 170, 220)
        label_hd(result_frame, marks_lst[1], 20, 'Blue', 170, 250)
        label_hd(result_frame, marks_lst[2], 20, 'Blue', 170, 280)
        label_hd(result_frame, marks_lst[3], 20, 'Blue', 170, 310)
        label_hd(result_frame, marks_lst[4], 20, 'Blue', 170, 340)

        label_hd(result_frame, f'{rank}', 30, 'Blue', 350, 220)
        label_hd(result_frame, grade_lst[2], 30, 'Blue', 350, 320)
        label_hd(result_frame, f'{grade_lst[1]}%', 30, 'Blue', 600, 220)
        label_hd(result_frame, grade_lst[0], 30, 'Blue', 600, 320)

        tk.Button(result_frame, text='Back', font='lucidia 25 bold', bg='yellow',
                  command=result_frame.destroy).place(
            x=300, y=400)

        tk.Button(result_frame, text='Export Data', font='lucidia 25 bold', bg='light green',
                  command=export_student).place(
            x=570, y=400)
        tk.Button(result_frame, text="Help", font='lucidia 10 bold', bg="red",
                  command=lambda: os.startfile('help me\\download.png')).place(x=750, y=5)

    except:
        messagebox.showerror("Error", 'Specified Name is Not found')
        result_frame.destroy()


def export_student():
    global path_box_ex
    export_fr = tk.Frame(root)
    export_fr.place(x=0, y=0, width=800, height=500)
    pic_label1 = tk.Label(export_fr, image=pic9).place(x=0, y=0, relheight=1, relwidth=1)
    tk.Label(export_fr, text="Enter Path for Exporting Data", font="lucidia 25 bold").place(x=100, y=70)
    path_box_ex = tk.Entry(export_fr, font="lucidia 20 bold", width=40)
    path_box_ex.place(x=50, y=160)
    tk.Button(export_fr, text="Export", font="lucidia 30 bold", bg='light green', command=data_Series_converter).place(
        x=200,
        y=270)
    tk.Button(export_fr, text="Back", font="lucidia 30 bold", bg='yellow', command=export_fr.destroy).place(x=500,
                                                                                                            y=270)
    tk.Button(export_fr, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\exporting data.png')).place(x=750, y=5)


def data_Series_converter():
    try:
        path = path_box_ex.get()
        dataname = tc.get()
        student = name_of_student.get()
        f = open(f"Data\\{dataname}\\{student}\\marks.txt", 'r')
        index_list = ['Maths', 'Physics', 'Chemistry', 'English', 'Optional']
        marks = f.read()
        marks_list = list(marks.split(","))
        data_ser = pandas.Series(marks_list, index=index_list)
        data_ser.name = 'Marks'
        print(data_ser)

        os.mkdir(f'{path}\\{student}')
        data_ser.to_csv(f'{path}\\{student}\\result.csv')
        shutil.copy(f'Data\\{dataname}\\{student}\\{student} Marks Bar Graph.png', f'{path}\\{student}')
        shutil.copy(f'Data\\{dataname}\\{student}\\{student} Marks Line Graph.png', f'{path}\\{student}')
        f.close()
        messagebox.showinfo('Successful', f'Data of Student {student} has been exported successfully')
    except:
        messagebox.showerror('Error', 'Specified Path is Incorrect')


def arranged_data():
    frame_arrageddata = tk.Frame(root)
    frame_arrageddata.place(x=0, y=0, width=800, height=500)
    database = tc.get()
    pic_label1 = tk.Label(frame_arrageddata, image=pic5).place(x=0, y=0, relheight=1, relwidth=1)
    box = tk.Text(frame_arrageddata, font="lucidia 25 bold", width=150, height=10, background="light blue")
    box.place(x=0, y=50)
    label_hd(frame_arrageddata, 'Rank Wise Categorised', 30, None, 200, 0)
    tk.Button(frame_arrageddata, text='Back', font='lucidia 25 bold', bg='light blue',
              command=frame_arrageddata.destroy).place(
        x=300, y=435)
    tk.Button(frame_arrageddata, text="Help", font='lucidia 10 bold', bg="red",
              command=lambda: os.startfile('help me\\download.png')).place(x=750, y=5)

    marks_dct = {}
    ranked_dct = {}
    name_list = os.listdir(f"Data\\{database}")

    # Mining total marks from txt file and getting them in dictionary
    for name1 in name_list:
        f = open(f"Data\\{database}\\{name1}\\grade.txt", "r")
        grade = list(f.read().split(","))
        total_marks = grade[1]
        marks_dct[name1] = total_marks

    # Making a new dictionary with ranked students
    sorted_key = sorted(marks_dct, key=marks_dct.get)
    x = len(list(range(len(marks_dct), 0, -1))) + 1
    for i in sorted_key:
        ranked_dct[i] = marks_dct[i]

        x = x - 1
        box.insert(1.0, f'\n-------------------------------------------------\n{x} )            {i}')

    box.insert(1.0, 'Rank       Name')
    print(x)



# Main code ============================================================================================================

root = tk.Tk()

# Window designer
root.geometry("800x500")
root.title("Result Analysis Creator")
root.resizable(False, False)  # resizeable false
root.iconbitmap("Resources\\window_ico.ico")

frame1 = tk.Frame(root).place(x=0, y=0, width=800, height=500)
pic8 = ImageTk.PhotoImage(file='Resources\\bg8.png')
pic_label1 = tk.Label(frame1, image=pic8).place(x=0, y=0, relheight=1, relwidth=1)
credit_label = tk.Label(root, text='\t\t\t\tCreated by Manas Bisht and Ishan Bijlani class 12th SPS RN\t\t\t\t\t\t',
                        font='lucidia 10 bold').place(x=0, y=480)

button(frame1, "     Data Creator     ", 25, "light blue", None, 0, 0, 247, 50, dataCreater_form)
button(frame1, "Show All Databases", 25, "light green", None, 1, 0, 247, 25, continue_dataShow)
button(frame1, "     Data Remover     ", 25, "red", None, 2, 0, 247, 55, dataRemover_form)
tk.Button(frame1, text="Help", font='lucidia 10 bold', bg="red",
          command=lambda: os.startfile('help me\\first form.png')).place(x=750, y=5)

# Backgrounds images for main form
pic1 = ImageTk.PhotoImage(file='Resources\\cm.png')
pic2 = ImageTk.PhotoImage(file='Resources\\3744.png')
pic3 = ImageTk.PhotoImage(file='Resources\\bg2.png')
pic4 = ImageTk.PhotoImage(file='Resources\\bg3.png')
pic5 = ImageTk.PhotoImage(file='Resources\\bg4.png')
pic6 = ImageTk.PhotoImage(file='Resources\\bg5.png')
pic7 = ImageTk.PhotoImage(file='Resources\\bg7.png')
pic9 = ImageTk.PhotoImage(file='Resources\\bg9.png')
pic10 = ImageTk.PhotoImage(file='Resources\\bg10.png')
pic11 = ImageTk.PhotoImage(file='Resources\\bg11.png')

# Help images for help widgets
first_pic = ImageTk.PhotoImage(file='help me\\first form.png')
second_pic = ImageTk.PhotoImage(file='help me\\second form.png')
entry_pic = ImageTk.PhotoImage(file='help me\\entry form.png')
main_pic = ImageTk.PhotoImage(file='help me\\main functions.png')
stud_exp = ImageTk.PhotoImage(file='help me\\exporting data.png')
stud_name_pic = ImageTk.PhotoImage(file='help me\\student.png')
# For result frame

root.mainloop()
