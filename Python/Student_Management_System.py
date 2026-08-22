while True:
    print("===== Student Management =====")
    print("1. Add Student")
    print("2. Show Student")
    print("3. Edit")
    choice=int(input("0. Exit\n"))
    if choice == 0:
        break

class Student:
    def __init__(self,Name,rollno,marks,cgpa):
        self.Name=Name
        self.rollno = rollno
        self.marks = marks
        self.cgpa = cgpa
    def show(self):
        if isinstance(self.Name,(str)):
            print("Your name is",self.Name)
        else:
            print("Invalid data")
        if isinstance(self.rollno,(int)) and self.rollno>0:
            print("Roll no:",self.rollno)
        else:
            print("Invalid data")
        if isinstance(self.marks, (dict)):
            for key, value in self.marks.items():
                print(key,"=",value)
        if isinstance(self.marks,(int,float)) and self.marks>0:
            print("Marks:",self.marks)
        if isinstance(self.cgpa,(float,int)) and self.cgpa> 0:
            print("CGPA:",self.cgpa)
        else:
            print("Invalid data")


s1 = Student("Zain",81,{"Math":89,"Chem":49,"Comp":24},3.40)
s1.show()