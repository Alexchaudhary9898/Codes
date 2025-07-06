from tkinter import *
from datetime import date
root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')
lbl = Label(text="hey there!",fg="white", bg="#072f5f", height=1, width=300)
name_entry = Entry()
def display():
    name = name_entry.get()
    global Message
    message = "welcome to the applications \n today's date is:"
    greet = "hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height=3)
btn = Button(text="begin", command=display, height=1, bg="#126140", fg='white')
lbl.pack()
name_entry.pack()
text_box.pack()
root.mainloop()