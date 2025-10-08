# class Student:
#     def __init__(self, name, rollno, marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks

# s1=Student("Durga" , 101 , 90) 
# print(s1.name, s1.rollno, s1.marks)





# class Student:
#     ''' This is Student class with required data '''           #------->  doc string
#     def __init__(self, name, rollno, marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#     def display(self):
#         print("The student name is {} , Student rollno is {} and Student marks is {}".format(self.name,self.rollno, self.marks))

# s1= Student("Durga" , 101, 99)
# print(s1.__doc__)  #----------->  This is Student class with required data
# s1.display() #------------------->  The student name is Durga , Student rollno is 101 and Student marks is 99










# class Test:
#     x=10
#     def __init__(self):
#         self.y=20

# t1=Test()
# t2=Test()
# print(t2.x)
# Test.x=222
# print(Test.__dict__)






# Instance method


# class Test:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
    
#     def m1(self):
#         print("Hi", self.name)
#         print("Your name:", self.name)
#         print("Your marks :", self.marks)

#     def grade(self):
#         if self.marks>60:
#             print("You got 'A' Grade")
#         elif self.marks>50:
#             print("You got 'B' Grade")
#         elif self.marks>=35:
#             print("You got 'C' Garde")
#         else:
#             print("You are failed...")


# n=int(input("Enter the number of students: "))
# for i in range(n):
#     name=input("Enter Student name: ")
#     marks=int(input("Enter Student Marks: "))
#     s1=Test(name,marks)
#     s1.m1()
#     s1.grade()



#Getter and setter method 


class Student:
    def setName(self, name):
        self.name=name
    def getName(self):
        return self.name
    
    def setMarks(self, marks):
        self.marks=marks
    def getMarks(self):
        return self.marks    
    

n=int(input("Enter the Number of student: "))
for i in range(n):
    s=Student()
    name=input("Enter student name: ")
    s.setName(name)
    marks=int(input("Enter student marks: "))
    s.setMarks(marks)

    print("HI", s.getName())
    print("Your Marks are: ", s.getMarks())