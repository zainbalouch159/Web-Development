totdata = int(input("How many employee data you want to store "))
keys = int(input("How many data in one employee profile "))
marks= [totdata]
for data in range(totdata):
    marks[data] = input(f"Enter data:  {data} ")
    for key in range(keys):
        print(f"<<{data}>>")
