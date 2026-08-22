class Student:
    
    def add_student(self):
        self.name = input("\nEnter student name: ")
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
            print("\nYour name is",self.name)
        else:
            print("Invalid data")

        if isinstance(self.rollno,(int)) and self.rollno>0:
            print("Roll no:",self.rollno)
        else:
            print("Invalid data")

        if isinstance(self.marks, (dict)):
            for key, value in self.marks.items():
                print(key,"=",value)

        if isinstance(self.cgpa,(float,int)) and self.cgpa> 0:
            print("CGPA:",self.cgpa)
        else:
            print("Invalid data")
            
    def edit(self):
        edit_name = input("Which student data you want to edit? ")
        choice = int(input("What you want to edit?\n 1: Name\n 2: roll No\n 3: Marks \n 4: CGPA \n 5: Back"))
        for student in new_student:
            if student.name == self.edit_name:
                match choice:
                    case 1:
                        new_name = input("Enter new name ")
                        student.name=new_name
                    case 2:
                        new_rollno = int(input("Enter new roll no "))
                        student.rollno=new_rollno
                    case 3:
                        for key, value in student.marks.items():
                            print(key,"=",value)
                        key_name = input("Enter name that you want to edit ")
                        key_reference = input("You want to edit data name or acutal data\n Press 1 for data name\n Press 2 for actual data")
                        match key_reference:
                            case 1:
                                pass

total_student = []

while True:
    print("\n===== Student Management =====\n")
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
        
        case 3:
            pass

    if choice == 0:
        break
