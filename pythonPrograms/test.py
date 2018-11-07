class clsA:
    def __init__(self):
        print("Init of A")
    def myMethod(self):
        print("myMethod A")

class clsB:
    def __init__(self):
        print("Init of B")
    def myMethod(self):
        print("myMethod B")

class clsC(clsB,clsA):
    def __init__(self):
        print("Init of C")
    #def myMethod(self):
    #    print("myMethod C")

ob = clsC()
ob.myMethod()
