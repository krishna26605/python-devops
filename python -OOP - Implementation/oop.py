
#///////////////////////////////CLASSES AND OBJECTS /////////////////////////////
class Students:
    def __init__(self ,name, marks ):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum= sum+val
        print("avg score of", self.name ,  "is", sum/3)

    @staticmethod      #STATIC DECORATOR
    def hello():
        print("HELOOOOOOOOOO")



s1= Students("krishna" , [90 , 30 , 56])
s1.get_avg()
        

s2= Students("niki" , [90 , 90 , 96])
s2.get_avg()


s1.hello()


#///////////////////// ABSTRACTION EXAMPLE ////////////////////////////////////////////
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def startcar(self):
        self.clutch = True
        self.acc = True
        print("Car Started ....")


s1 = Car()
s1.startcar()


#////////////////////////ACCOUNT - BANK - EXAMPLE //////////////////////////////


class Account:
    def __init__(self , bal , accno):
        self.accno= accno
        self.bal= bal
        

    def debit(self , amount):
        self.bal= self.bal-amount
        print("rs debit is ", amount, "from your bank account")
        print("your remaining balance is " , self.bal)

    def credit(self , amount):
        self.bal= self.bal+amount
        print("rs credit is ", amount, "to your bank account")
        print("your remaining balance is " , self.bal)


s1= Account(20000 , 2345)
s1.debit(2000)
s1.credit(3000)


#////////////////////////////PUBLIC & PRIVATE ATTRIBUTES /////////////////////////////


class Accounts:
    def __init__(self , accno , accpass):
        self.accno=accno
        self.__accpass=accpass              #////// by double underscore(__) in front of attribute makes it private attribute can't access outside the class but can be accessible inside class 


acc1=Accounts(1234 , "pased@2022")
print(acc1.accpass)
print(acc1.accno)



#//////////////////////////////INHERITANCE EXAMPLE /////////////////////////////////////////////

class Car:
    color = "black"
    @staticmethod
    def startcar():
        print("Car Started .........")

    @staticmethod
    def stopcar():
        print("Car Stopped .........")


class ToyotaCar(Car):
    def __init__(self , carname):
        self.carname=carname
        

car1= ToyotaCar("fortuner")
car2= ToyotaCar("pruis")

print(car1.startcar())
print(car1.color)

#///////////////  MULTIPLE INHERITENCE EXAMPLE /////////////////////////////////


class A:
    varA = "This is class A"

class B:
    VarB = "THis is class B"

class C (A , B):
    varC = "Welcome to class C"


c1= C()
print(c1.varA)
print(c1.VarB)
print(c1.varC)


#//////////////////////////////////////  SUPER METHOD /////////////////////////////////////////


class Car:

    def __init__(self , type):
        self.type = type
        
    
    @staticmethod
    def startcar():
        print("Car Started .........")

    @staticmethod
    def stopcar():
        print("Car Stopped .........")


class ToyotaCar(Car):
    def __init__(self , carname , type):
        self.carname=carname
        super().__init__(type)
        super().startcar()

        

car1 = ToyotaCar("Fortuner", "Diesel")
print(car1.type)

# ///////////////////////////////////  CLASS METHOD ///////////////////////////////////////////////////


class Person:
    name = "Anonmous"


    @classmethod
    def changeName(cls , name):
        cls.name = name


    # def changeName(self , name):
    #     self.__class__.name = name              # self.__class__  to change class attribute from function 

                                                  # @classmethod is used to change the class attribute which is not done by @staticmethod
    

p1 = Person()
p1.changeName("Krishna Nikam")
print(p1.name)
print(Person.name)



# 1].  Static Method   ()
# 2].  class method  (cls)
# 3].  instance method  (self)



#/////////////////  PROPERTY DECORATOR ////////////////////////////////////////////////

class Student:
    def __init__(self, phy , chem , math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property                                                # @property ke wajah se automatically percentage change hojayenge if marks change hue to 
    def percentage(self):                                    
        return str((self.phy+self.chem+self.math)/3) + "%"


stu1= Student(78 , 45 , 89)

stu1.chem=90
print(stu1.percentage)



#///////////////////////////////////////   POLYMORPHISM  ///////////////////////////////////////////////////////////


# one of the comman example of polymorphism is operator overloading (same operator have different meanings according to context)


print(1+2) #3
print("over" + "loading") #overloading
print([1 , 2 , 3] + [4 , 5 ,3])  #merge [1 , 2 , 3 , 4 , 5 , 3]







#////////////////////////  DUNDER FUNCTIONS  //////////////////////////////////////////


class Complex:
    def __init__(self , real , img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real , "i +" ,  self.img , "j")

    def __add__(self , num2):
        newReal = self.real + s2.real
        newImg = self.img + s2.img
        return Complex(newReal , newImg)

s1 = Complex(2 , 4)
s2 = Complex(5 , 6)
s1.showNumber()
s2.showNumber()
s3 = s1 + s2 
s3.showNumber()