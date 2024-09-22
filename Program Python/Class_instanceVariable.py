# creating a class and instance variable
class Student:
    def __init__(self,name,rollno):
        self.name=name # self.name is a instance variable
        self.rollno=rollno # self.rollno is a instance variable
    def prop(self):
        del self.name
        print("student rollno is",self.rollno)
s1=Student("will smith",201)
s1.prop()
# accessing instobject referenceance variable with 
s1.age=30
print(s1.__dict__)
print()
# we can also delete instance variable
print()
s2=Student('roy',34)
print(s2.__dict__)
s2.prop()
print(s2.__dict__)



