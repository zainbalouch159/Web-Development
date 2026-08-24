
total_student = []
class Student:
    
    def add_student(self): # -->  Student add fun
        while True:
            self.name = input("\nEnter student name: ")
            if self.name.isalpha():
                break
            else:
                print("\nEnter valid name")
            
        while True:
            try:
                self.rollno = int(input("\nEnter roll no: "))
               
                if self.rollno>0 and self.rollno<100:
                    break
                else:
                    print("\nInvalid roll no")
            except ValueError:
                            print("\nInvalid roll no")
            
        while True:
            try:    
                total_subject = int(input("\nHow many subject in last semester: "))
                if total_subject>10 or total_subject<1:
                    print("\nInvalid input")
                else:
                    break
            except ValueError:
                print("\nInvalid input")
        
        self.marks = {}
        
        for i in range(total_subject):
            print("\n\t<<(",i+1,")>>")
            while True:
                subject_name=input("\nEnter subject name of last semester: ")
                if subject_name.isalpha():
                    break
                else:
                    print("\nPlease enter text")
            while True:
                try:
                    subject_marks= int(input(f"\nHow many marks you got in {subject_name}: "))
                    if subject_marks>100 or subject_marks<0:
                        print("Invalid input")
                    else:
                        self.marks[subject_name]=subject_marks
                        break
                except ValueError:
                    print("\nInvalid input")
        while True:
            try:
                self.cgpa= float(input("\nWhat your cgpa: "))
                if self.cgpa>4 or self.cgpa<0:
                    print("\nInvalid input")
                else:
                    break
            except ValueError:
                print("\nInvalid input")
                
    def marks_edit(self): # ---> Marks edit fun
        
     while True: # 4 
            print("\n")
            
            for key, value in self.marks.items():
                print(key,"=",value)
                
            while True: # 5
                key_name = input("\nEnter name that you want to edit ")
                if key_name.isalpha():
                    break # Terminate 5
                else:
                    print("\nPlease enter text")
        
            if key_name in self.marks:
                value = self.marks[key_name]
                while True: # 7 
                    try:
                        key_reference = int(input("\nYou want to edit data name or acutal data\nPress 1 for data   name\nPress 2  for actual data\n"))
                        break # Terminate 7
                    except ValueError:
                        print("\nInput invalid")
        
                match key_reference:
                    case 1:
                        while True: # 8
                            new_key= input(f"\nEnter name that you want to replace with {key_name} ")
                            if new_key.isalpha():
                                self.marks[new_key]=value
                                del self.marks[key_name]
                                break # Terminate 8
                            else:
                                print("\nPlease enter text")
        
                        break # Terminate 4
        
                    case 2:
                        while True:
                            try:
                                new_value= int(input(f"\nEnter data that you want to replace wit {value}"))
                                self.marks[key_name]=new_value
                                break
                            except ValueError:
                                print("Invalid input")     
            else:
                print("\nNo data with ",key_name," such name exists")
            
    def edit(self): # --> Student info edit fun
        while True: # -> 1
            try:
                choice = int(input("\nWhat you want to edit?\n 1: Name\n 2: roll No\n 3: Marks \n 4: CGPA \n 5: Back\n"))
                break # -> Terminate 1
            except ValueError:
                print("\nInvalid input")
        match choice:
            case 1:
                while True: # -> 2
                    new_name = input("\nEnter new name ")
                    if new_name.isalpha():
                        self.name=new_name
                        break # -> Terminate 2
                    else:
                        print("\nPlease enter text")
                        
            case 2:
                while True: # 3
                    try:
                        new_rollno = int(input("\nEnter new roll no "))
                        if new_rollno>0 and new_rollno<100:
                            self.rollno=new_rollno
                            break # -> Terminate 3
                        else:
                            print("\nInvalid roll no")
                    except ValueError:
                        print("\nInvalid input")
                
            case 3:
                self.marks_edit()
                               
            case 4:
                while True:
                    try:
                        new_cgpa = float(input(f"\nEnter new CGPA that you want to replace with {self.cgpa} "))
                        if new_cgpa>4 or new_cgpa<0:
                            print("Invalid input")
                        else:         
                            self.cgpa= new_cgpa
                            break
                    except ValueError:
                        print("\nInvalid input")
                        
    def show(self): # --> Student info show fun

            print("\nYour name is",self.name)

            print("\nRoll no:",self.rollno)

            print("\n===== Marks =====\n")
            for key, value in self.marks.items():
                print(key,"=",value)

            print("\nCGPA:",self.cgpa)
            
while True: # --> Main Menu 
    while True:
        try:
            print("\n===== Student Management =====\n")
            print("1. Add Student")
            print("2. Show Student")
            print("3. Edit")
            choice=int(input("0. Exit\n"))
            break
        except ValueError:
            print("\nInvalid input")
    
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
                print("\nNo student record is saved")
        
        case 3:
            if len(total_student)>1:
                for student in total_student:
                    print(student.name)
                while True:
                    edit_name = input("\nWhich student data you want to edit? ")
                    if edit_name.isalpha():
                        break
                    else:
                        print("\nPlease enter text")
                for student in total_student:
                    if student.name == edit_name:
                        student.edit()
                        break
                else:
                    print("\nNo such name ", edit_name," exists")
            elif len(total_student)<1 :
                 print("\nNo student record is saved")
            elif len(total_student)==1:
                total_student[0].edit()
            
        case 0:
            break
    
print("\nExit Successfully")
