class IOString():
    def __init__(self):
        self.strl = ""
    def get_String(self):
        self.strl = input("enter string : ")
    def print_String(self):
        print("result is :", self.strl.upper())
strl = IOString()
strl.get_String()
strl.print_String()