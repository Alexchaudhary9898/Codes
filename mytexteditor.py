from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("Condigal's text editor")
window.geometry("600x500")
window.rowconfigure(0, minisize=800, weight=1)
window.columnconfigure(1, minisize=800, weight=1)
def open_file():
    """Open a file for editing"""
    filepath = askopenfilename(
        filetypes=[("text files", "*.txt"), ("all files", "*.*")]
    )
    if not filepath:
            return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
          text = input_file.read()
          txt_edit.insert(END, text)
          input_file.close()
    window.title(f"Codingal's text editor - {filepath}")
def save_file():
      filepath = asksaveasfilename(
            defaultextensions="txt",
            filetypes=[("text files", "*.txt"), ("all files","*.*")],
      )
      if not filepath:
            return
      with open (filepath, "w") as output_file:
          text = txt_edit.get(1.0, END)
          output_file.close()
    window.title(f"Codingal's Text editor - {filepath}")
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save as...", command=save_file)