# class Student:
#     name = "Hamza"
#     rollno = None
#     cgpa = None
#     uni = "USP"
#     __fail= "Math"
#     @staticmethod #decorator
#     def greet():
#         print("Hello")
#     def __init__(self, name=None,__Pass="Phy"):
#         print("Hello "+ name)
#     # def __init__(self):
#     #     print("Constructor called")
#     def show(self):
#         print(f"Your name is {self.name} and your roll no is {self.rollno } and your cgpa is {self.cgpa}")
# s1= Student("Zain")
# s1.name="Zain"
# s1.rollno=81
# s1.cgpa= 2.2
# s1.show()
# s2=Student("Zain")
# print(type(s1.cgpa))
# print(Student.uni)
# s1.greet()
# # s1.__fail
# s1.__Pass

class studen:
    def __init__(self,name=None,rollno=None,cgpa=None):
        self.name=name
        self.rollno=rollno
        self.cgpa=cgpa
    def hello(self):
        print("Hello")
class person(studen):
    pass
    def __init__(self):
        super().hello()
        print("Child")
s1 = person()
# del s1.name
# print( s1.name, s1.rollno,s1.cgpa)
# s1.helloello()