# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
    y=10
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.  #usually class methods are used as factory methods
    @classmethod
    def fromBirthYear(cls, name, year):
        print(cls.y)
        return cls(name, date.today().year - year)

    #just lile utility fun take, cannot access self
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

