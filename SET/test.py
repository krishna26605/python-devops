dict={}
n= int(input("Enter the number of students:"))
i=1
while i<=n:
    name=input("Enter the student name: ")
    marks=input("Enter the student marks: ")
    dict[name]=marks
    i=i+1
print(dict)