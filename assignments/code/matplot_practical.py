
#program2

#Write a python program to create bar chart for result 
#of a student in 5 subjects in UT1, UT2, UT3 and MT1
import matplotlib.pyplot as plt
import numpy as np
plt.figure(facecolor='black')
sub=['maths ','ip','english','hindi','socials']
sub_marks_ut1=[64,75,82,92,87]
sub_marks_ut2=[92,52,72,62,72]
sub_marks_ut3=[52,72,52,72,72]
a = np.arange(len(sub))


plt.bar(a,sub_marks_ut1,width= 0.25)
plt.bar(a+0.5,sub_marks_ut2,width=0.25)

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


plt.show()

#1. Write a python program for result analysis - performance of the students on different parameters subject wise and class wise : Bar Chart

plt.figure(facecolor='black')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

w=0.3
sub=['maths ','ip','english','hindi','socials']
student1=[89,45,67,87,33]
student2=[23,54,76,37,92]
student3=[82,34,80,23,3]

x = np.arange(len(sub))
plt.bar(x+0.0,student1,w,color='yellow',label="student1")
plt.bar(x+0.25,student2,w,color='red',label="student2")
plt.bar(x+0.50,student3,w,color='green',label="student3")


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


plt.xticks(x,sub)
plt.legend()
plt.show()
