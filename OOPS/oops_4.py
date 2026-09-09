#Attributes
class Student:
    pass

student1 = Student()
student2 = Student()

student1.name = "John"
student1.roll = 101

print(student1.name)
print(student1.roll)
print(student1.__dict__) # it stores values in dictionary