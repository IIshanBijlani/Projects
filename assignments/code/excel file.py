# Excel pandas and csv things

import os
import pandas
import getpass
import matplotlib.pyplot as plt
import numpy as np


# Will convert marks of particular student in Series===========================================================
def Data_Series_converter(dataname, student):
    f = open(f"Data\\{dataname}\\{student}\\marks.txt", 'r')
    index_list = ['Maths', 'Science', 'Sst', 'English', 'Hindi']
    marks = f.read()
    marks_list = list(marks.split(","))
    data_ser = pandas.Series(marks_list, index=index_list)
    print(data_ser)
    f.close()


# Data_Series_converter("Report class 10th", "agam")


# This function will creat a dataframe of all names given in a report folder=======================================
def Report_Frame_converter(dataname):
    student_names_list = os.listdir(f"Data\\{dataname}")
    dct = {}

    # This loop will convert all name and marks into dictionary
    for name in student_names_list:
        f = open(f"Data\\{dataname}\\{name}\\marks.txt", 'r')
        marks = f.read()
        dct[name] = list(marks.split(","))

    # Above mined data will be converted into dataframe
    Dataframe = pandas.DataFrame(dct, index=['Maths', 'Science', 'Sst', 'English', 'Hindi'])
    transposed_df = Dataframe.T
    print(transposed_df)


# It will convert data in excel sheet aka csv file
def Csv_converter(dataname):
    student_names_list = os.listdir(f"Data\\{dataname}")
    dct = {}

    # This loop will convert all name and marks into dictionary
    for name in student_names_list:
        f = open(f"Data\\{dataname}\\{name}\\marks.txt", 'r')
        marks = f.read()
        dct[name] = list(marks.split(","))

    # Above mined data will be converted into dataframe
    Dataframe = pandas.DataFrame(dct, index=['Maths', 'Science', 'Sst', 'English', 'Hindi'])
    transposed_df = Dataframe.T
    transposed_df.to_csv(f"C:\\Users\\{getpass.getuser()}\\Documents\\{dataname}.csv")
