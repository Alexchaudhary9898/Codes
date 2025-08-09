import matplotlib.pyplot as plt
students_names=["sanjay","rahul","karan","wasim","ramesh","ajay","sarta","priya"]
students_marks=[35,50,20,45,25,40,25,40]
marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)
def marks_line_chart():
    plt.plot(students_names,students_marks)
    plt.title("students names")
    plt.xlabel("students names")
    plt.ylabel("students marks")
    plt.show()
marks_line_chart()