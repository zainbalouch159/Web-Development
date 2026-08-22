totdata = int(input("How many employees data you want to store "))
keys = int(input("How many data in one employee profile "))
marks = []
for data in range(totdata):
    employee = {}
    for keycount in range(keys):
        print(f"<<{data+1}.{keycount+1}>>")
        key = input("Enter data name ")
        value= input("Enter acutal data ")
        employee[key]=value
    marks.append(employee)
print(marks)    