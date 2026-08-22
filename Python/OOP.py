# # class Student:
# #     name = "Hamza"
# #     rollno = None
# #     cgpa = None
# #     uni = "USP"
# #     __fail= "Math"
# #     @staticmethod #decorator
# #     def greet():
# #         print("Hello")
# #     def __init__(self, name=None,__Pass="Phy"):
# #         print("Hello "+ name)
# #     # def __init__(self):
# #     #     print("Constructor called")
# #     def show(self):
# #         print(f"Your name is {self.name} and your roll no is {self.rollno } and your cgpa is {self.cgpa}")
# # s1= Student("Zain")
# # s1.name="Zain"
# # s1.rollno=81
# # s1.cgpa= 2.2
# # s1.show()
# # s2=Student("Zain")
# # print(type(s1.cgpa))
# # print(Student.uni)
# # s1.greet()
# # # s1.__fail
# # s1.__Pass

# # Multilevel Inheritance

# # class student:
# #     def __init__(self,name=None,rollno=None,cgpa=None):
# #         self.name=name
# #         self.rollno=rollno
# #         self.cgpa=cgpa
# #     def hello(self):
# #         print("Hello")
# # class person(student):
# #     def show(self):
# #         print("Namaste")
# # class insan(person):
# #     def __init__(self):
# #         super().__init__( )
# #         super().hello()
# #         print("Child")
# # s1 = insan()
# # # del s1.name
# # print( s1.name, s1.rollno,s1.cgpa)
# # print("Hello")
# # s1.show()

# class A:
#     name = "anonymous"
#     def show(self):
#         print("Hello")
# class B:
#     full_name ="unknown"
#     def show(self):
#         print("Assalam o Alikum")
#     @classmethod
#     def change(cls,name):
#         cls.full_name= name
# class C(B,A):
#     pass
#     # def nameshow(self, name):
#     #     # A.name= name
#     #     self.__class__.name= name
# s1= B()
# s2= B()
# # s1.show()
# s1.change("Zain")
# # print(A.full_name)
# print(B.full_name)
# print(s1.full_name)
# print(s2.full_name)
# # s1.display()

class complex:
    def __init__(self, real, img):
        self.real= real
        self.img= img
    def __add__(self,obj2):
        real = self.real + obj2.real
        img = self.img + obj2.img
        return complex(real,img)
    def show(self):
        print(self.real,"i + ",self.img,"j")
        
num1 = complex(23,2)
num1.show()
num2 = complex(24,9)
num2.show()
num3 = num1+num2
num3.show()    