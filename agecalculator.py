import tkinter as tk
from datetime import datetime
def calculate_age():
    try:
        dob = datetime.strip(entry.get(). "%d/%m/%y")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month. dob.day))
        result.config(text=f"Age: {age} years")
    except:
        result.config(text="Enter date as DD/MM/YYYY")
root = tk.Tk()
root.title("age calculator")
tk.label(root, text="enter DOB (DD/MM/YYYY):").pack()
entry.pack()
tk.Button(root, text="calculator age", command=calculate_age).pack(pady=5)
result = tk.label(root, text="")
result.pack()
result.mainloop()