class Student:
    def __init__(self):
        self.__marks = 90   # private variable

s = Student()

# Accessing private variable using name mangling
print("Marks:", s._Student__marks)