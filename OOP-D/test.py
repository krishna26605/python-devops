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










class Test:
    x=10
    def __init__(self):
        self.y=20

t1=Test()
t2=Test()
print(t2.x)
Test.x=222
print(Test.__dict__)
