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


# class Student:
#     def setName(self, name):
#         self.name=name
#     def getName(self):
#         return self.name
    
#     def setMarks(self, marks):
#         self.marks=marks
#     def getMarks(self):
#         return self.marks    
    

# n=int(input("Enter the Number of student: "))
# for i in range(n):
#     s=Student()
#     name=input("Enter student name: ")
#     s.setName(name)
#     marks=int(input("Enter student marks: "))
#     s.setMarks(marks)

#     print("HI", s.getName())
#     print("Your Marks are: ", s.getMarks())




#CLASS METHOD

# class Animal:
#     legs=4
#     @classmethod
#     def walk(cls,name):
#         print("{} walks by {} legs".format(name,cls.legs))

# a=Animal()
# a.walk("Lion")
# a.walk("cat")




#WAP: To track the number of object created...


# class Test:
#     count=0
#     def __init__(self):
#         Test.count=Test.count+1
#     @classmethod
#     def noOfObject(cls):
#         print("The number of objects created are: ", cls.count)
# t1=Test()
# t2=Test()
# t5=Test()

# Test.noOfObject()       #-------------->  The number of objects created are:  3













# ONE CLASS METHOD CAN BE ACCESS IN ANOTHER CLASS:



# class Students:
#     def __init__(self,sno, sname, smarks):
#         self.sno=sno
#         self.sname=sname
#         self.smarks=smarks

#     def display(self):
#         print("The Student no is",self.sno)
#         print("The Student name is",self.sname)
#         print("The Student marks are",self.smarks)


# s= Students(101,"Durga", 90)

# class Test:
#     def modify(s):
#         s.smarks=e.smarks+1
#         s.display()

# Test.modify(s)







# class Person:
#     def __init__(self):
#         print("Person class constructor called....")
#         self.name="Krishna"
#         self.db= self.Dob()
#     def display(self):
#         print("Name:", self.name)

#     class Dob:
#         def __init__(self):
#             print("DOB class constructor called....")
#             self.dd=26
#             self.mm=6
#             self.yy=2005
#         def display(self):
#             print("DOB: {}/{}/{}".format(self.dd,self.mm,self.yy))


# t=Person()  #-------->  Person class constructor called....
#                         #@DOB class constructor called....
# t.display()  #-------->  Name: Krishna
# t.db.display()  #  ---------->  DOB: 26/6/2005








#COMPOSITION [Has-A-Relationship]




# class Car:
#     def __init__(self,name,brand,color):
#         self.name=name
#         self.brand=brand
#         self.color=color
#     def displayCarInfo(self):
#         print("Car Name is {}\nCar Brand is {}\nCar Color is {}".format(self.name,self.brand,self.color))



# class Employee:
#     def __init__(self,ename,eComName, car):
#         self.ename=ename
#         self.eComName=eComName
#         self.car=car

#     def empInfoDisplay(self):
#         print("Employee Name: {}\nEmployee Company Name: {}\n".format(self.ename,self.eComName))
#         print("Employee Car Details: ")
#         self.car.displayCarInfo()

# c=Car("Verna", "Hyundai" , "Black")
# E=Employee("Krishna", "Siemens" , c)
# E.empInfoDisplay()














# INHERITENCE



class Parent:
    def __init__(self):
        print("Parent class Constructor..")

    def m1(self):
        print("M1 method of parent ..")


class Child(Parent):
    def __init__(slef):
        super().__init__()

        print("Child class Constructor")

    
    def m1(self):
        super().m1()
        print("Child class m1 method")

C=Child()
C.m1()