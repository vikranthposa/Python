class baseClass:
    argument=[]
    @classmethod
    def base_class_method(cls):
        a = cls()
        return a

    @staticmethod
    def base_static_method():
        a = baseClass()
        return a

class Derived(baseClass):
    pass

a = baseClass()
b = Derived()

print()
print("class method called by base class")
print(a.base_class_method())
print("class method called by Derived class")
print(b.base_class_method())

print()
print("static method called by base class")
print(a.base_static_method())
print("static method called by Derived class")
print(b.base_static_method())
