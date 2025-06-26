class Student:
    name="default"

# instance 
s1=Student()


print(s1.name)

class Car :
    color="blue"
car1=Car()
print(car1.color)

# constructor
class Student :
    def __init___(self):
        pass
    def __init__(self,fullname):
        self.name=fullname # attribute 


s1 =Student("ayush")
print(s1.name)

# Attributes 
# two types class.attr, obj.attr
class Student :
    college_name="DTU"
    name="anonymous"
    def __init__(self,name):
        self.name=name
    
s1=Student("ayushKumar")
print(s1.name) #obj attr>class attr
print(Student.name)
print(Student.college_name)

# Methods 
class Student :
    def __init__(self,name):
        self.name=name
    def hello(self):
        print("Wellcome", self.name)
s1=Student("ayush")
s1.hello()
#static methods
#don't use self param, work at class level

class Student :
    def __init__(self,name):
        self.name=name
    @staticmethod # decorator
    def hello():
        print("Wellcome")

#Abstraction

#Encapuslation
