# print("Zain","Balouch")
# name = "Zain"
# age = 22
# print(name,age)
# print(type(age))
# isalive = False
# print(isalive)
# name = input("Enter your name ")
# print("hello " + name) #Concatenation

# Type casting & Type conversion

# age = input("Enter your age ")
# age1=int(age)
# age1 = age1+1
# print(age1)
# print(float(age1)) # Type casting explicit
# print(bool(age1))
# print(str(age1))
# print(type(age1)) 
# print(2+2.5) # Type conversion implicit

# String Method

# name = "Zain Khan" 
# String are immutable
# print(name.upper())
# print(name)

# # Find 

# print(name.find("K"))

# Replace

# print(name.replace("Khan","Balouch"))

# Check for presence

# print("K" in name) # in is keyword 

# Artihmatic operators

# print(4+3)
# print(4-3)
# print(4*3)
# print(4/3)
# print(4//3)
# print(4%3) # Modulo-> Reminder
# print(4**3)

# assigment operator

# cgpa = 9.2
# cgpa = cgpa +2
# cgpa += 3
# print(cgpa)

# Operator Precedence
#   *,/ > +,-

# print(not(1>2))

# age = 188
# invite = True

# if age >18 and invite :
#     print("Allowed")
# elif age<18 or invite:
#     print("Not Allowed")
# else :
#     print("Youre 18")
# print("Zain")

# nums = range(9)
# print(nums)
# nums = range(2,9)
# print(nums)
# num = 2

# Loops


# while Counter <5:
# Counter = 1
#     print(Counter*"*")


#     Counter+= 1
# print("Finish")

# for loop

# nums = range(5)
# for i in range(0,9,2):
#     if i== 4:
#         continue
#     if i==8:
#         break
#     print(i)

# List 

# marks =["zain", 23,52,23,25]
# # print(marks)

# # # Length
# # print(len(marks))

# # # index
# # print(marks[-1])

# # # Slicing a list 
# # # print(marks[1:4])
# # print(marks[-2:])
# marks.append("Rehan")
# marks.insert(2,"Hamza")
# for count in range(len(marks)):
#     print(marks[count])
# print("Rehan" in marks, type(marks))
# marks.clear()
# print(marks)

# Tuple immutable

# marks =("zain", 23,52,23,25)
# print(marks.count(23))
# print(marks.index(23), type(marks))

# Set => Unique item collection

# marks = {52,2,23}
# print(marks)

# for mark in marks:
#     print(mark)

# Dictionary key => value , mutable

# marks = {"Math": 98, "Chemistry": 89, "Physics": 90, "Math": 88 }
# print(type(marks), marks)
# marks["Chemistry"]= 70
# print(marks["Chemistry"])

# Functions

# def add(a,b):
#     print(a+b)
# add(23,67)

# def fictorial(num):
#     if num>0:
#         return num*fictorial(num-1)
#     return 1


# print(fictorial(5))

# num = int(input("Kis number ka fictoril chia? "))
# fictorial = 1

# for rezutl in range(num,0,-1):
#     fictorial *= rezutl

# print(fictorial)

# def fun(num):
#     if num>0:
#         return num+fun(num-1)
#     return 1
# print(fun(5))
