class Student:
    
    def add_student(self):
        self.name = input("Enter student name: ")
        self.rollno = int(input("Enter roll no: "))
        total_subject = int(input("How many subject in last semester: "))
        
        self.marks = {}
        for i in range(total_subject):
            print("\t<<(",i+1,")>>")
            subject_name=input("Enter subject name of last semester: ")
            subject_marks= int(input(f"How many marks you got in {subject_name}: "))
            self.marks[subject_name]=subject_marks
            
        self.cgpa= float(input("What your cgpa: "))
        
    def show(self):
        if isinstance(self.name,(str)):
            print("Your name is",self.name)
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

total_student = []

while True:
    print("===== Student Management =====")
    print("1. Add Student")
    print("2. Show Student")
    print("3. Edit")
    choice=int(input("0. Exit\n"))
    
    match choice:
        case 1:
            new_student= Student()
            new_student.add_student()
            total_student.append(new_student)
        
        case 2:
            if total_student:
                for student in total_student:
                    student.show()

    if choice == 0:
        break

print(total_student)