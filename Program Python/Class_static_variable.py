class Student():
    cname="Ravenshaw"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
s1=Student('Raghav',101)
# accessing instance variable using only object 
print(s1.name)
print(s1.rollno)
# we can access static variable using object and also class name
print(s1.cname)
print(Student.cname)