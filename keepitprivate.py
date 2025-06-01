class myClass:
    __privateVar = 27;
    def __privMeth(self):
        print("im inside myClass")
    def hello(self):
        print("private variable valu: ".myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__privMeth