from tkinter import*
def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result.config(text=f"{cm:.2f} cm")
window = Tk()
window.title("inch to  CM")
entry = Entry(window)
entry.pack()
btn = Button(window, text="conver", command=convert)
btn.pack()
result = Label(window, text="")
result.pack()
window.mainloop()