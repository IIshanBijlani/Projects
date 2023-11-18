# data_creator tkinter

# data creater 2.0

import os
import shutil
import matplotlib.pyplot as plt
import tkinter as tk


# Calculate Grade of a student
def grade_calculator(percent):
    if 91 <= percent <= 100:
        return "Grade A1"
    elif 81 <= percent <= 90:
        return "Grade A2"
    elif 71 <= percent <= 80:
        return "Grade B1"
    elif 61 <= percent <= 70:
        return "Grade B2"
    elif 51 <= percent <= 60:
        return "Grade C1"
    elif 41 <= percent <= 50:
        return "Grade C2"
    elif 31 <= percent <= 40:
        return "Grade D"
    else:
        return "You failed"


# To create a folder of a data
def data_creator():
    dataname = entry1.get()
    os.mkdir(f"Data\\{dataname}")


# data_creator("Report class 10th")


# To remove a foldr of data
def data_remover(dataname):
    shutil.rmtree(f"Data\\{dataname}")


# To remove a perticular student
def student_remover(dataname, student_name):
    shutil.rmtree(f"Data\\{dataname}\\{student_name}")


# To add data report of students
def student_result(report,addmission_no, student_name ,gender, maths, science, sst, english, hindi):
    try:
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
        index_list = ['Maths', 'Science', 'Sst', 'English', 'Hindi']
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
        plt.close()

    except:
        print("SOmething is wrong")


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


# student_result("Report class 10th", "18671r", "Akshay","male", 1, 2, 1, 1, 4)
# student_result("Report class 10th", "18671r", "Agam", "male", 19, 9, 19, 71, 94)
# student_result("Report class 10th", "18671r", "Ishan", "male", 99, 98, 99, 75, 78)
# student_result("Report class 10th", "18671r", "Manas","male", 18, 98, 17, 99, 2)


root = tk.Tk()
root.geometry("500x300")
label1 = tk.Label(root, text="Enter name of New data", font="lucidia 25 bold").pack(pady=23)
entry1 = tk.Entry(root, font="lucidia 25 bold")
entry1.pack(pady=23)
button = tk.Button(root, text="Continue", font="lucidia 25 bold", bg="light blue", command=data_creator).pack(pady=23)
root.mainloop()

