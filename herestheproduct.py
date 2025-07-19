from tkinter import
def multiply():
    result = int(num1.get()) * int(num2.get())
    output.config(text="Product: " + str(result))
root = Tk()
root.title("Multiply numbers")
num1 = Entry(root)
num1.pack()

num2 = Entry(root)
num2.pack()
btn = Button(root. text="Multiply", command=multiply)
btn.pack()
output = Label(root)
output.pack()
root.mainloop()