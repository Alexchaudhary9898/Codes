from tkinter import*
def check_strength():
    password = entry.get()
    if len(password) < 6:
        result_label.config(text="weak")
    elif len(password) <= 10:
        result_label.config(text="medium")
    else:
        result_label.config(text="strong")
root = Tk()
root.title("password checker")
Label(root, text="enter password:").pack()
entry= Entry(root, show="*")
entry.pack()
Button(root, text="check strength", command=check_strength).pack()
result_label = Label(root, text="")
result_label = Label.pack()
root.mainloop()