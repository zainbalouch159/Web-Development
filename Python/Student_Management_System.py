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
            print("\n===== Marks =====\n")
            for key, value in self.marks.items():
                print(key,"=",value)

        if isinstance(self.cgpa,(float,int)) and self.cgpa> 0:
            print("\nCGPA:",self.cgpa)
        else:
            print("Invalid data")
            
    def edit(self):
        choice = int(input("What you want to edit?\n 1: Name\n 2: roll No\n 3: Marks \n 4: CGPA \n 5: Back\n"))
        
        match choice:
            case 1:
                new_name = input("Enter new name ")
                self.name=new_name
            case 2:
                new_rollno = int(input("Enter new roll no "))
                self.rollno=new_rollno
            case 3:
                for key, value in self.marks.items():
                    print(key,"=",value)
                key_name = input("\nEnter name that you want to edit ")
                for key, value in self.marks.items():
                    if key == key_name:
                        key_reference = int(input("You want to edit data name or acutal data\n Press 1 for data name\nPress 2  for actual data\n"))
                        match key_reference:
                            case 1:
                                new_key= input(f"Enter name that you want to replace with {key} ")
                                self.marks[new_key]=value
                                del self.marks[key]
                            case 2:
                                if isinstance(value,(int)):
                                    new_value= int(input(f"Enter data that you want to replace wit {value}"))
                                    self.marks[key]=new_value
                                if isinstance(value,(float)):
                                    new_value= float(input(f"Enter data that you want to replace wit {value}"))
                                    self.marks[key]=new_value
                                if isinstance(value,(str)):
                                    new_value= input(f"Enter data that you want to replace wit {value}")
                                    self.marks[key]=new_value
                        break       
            case 4:
                new_cgpa = float(input(f"Enter new CGPA that you want to replace with {self.cgpa} "))         
                self.cgpa= new_cgpa
            
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
            else:
                print("No student record is saved")
        
        case 3:
            if len(total_student)>1:
                for student in total_student:
                    print(student.name)
                edit_name = input("Which student data you want to edit? ")
                for student in total_student:
                    if student.name == edit_name:
                        student.edit()
                        break
            elif len(total_student)<1 :
                 print("No student record is saved")
            else:
                total_student[0].edit()
            
    if choice == 0:
        break
    
print("\nExit Successfully")
