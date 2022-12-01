
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks

    def display(self):
        print("Name    : " + self.name)
        print("Roll no : " + str(self.roll))
        print("Age     : " + str(self.age))
        print("Marks   : " + str(self.marks))


s1 = Student('Rudra',69)
s1.setAge(20)
s1.setMarks(98)
s1.display()