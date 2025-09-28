# def f1():
#     print("HELLO...")

# # f1()
# print(f1())



# def evenodd(n):
#     if n%2==0:
#         print("EVEN: ",n)
#     else:
#         print("odd: ", n)

# evenodd(10.4)
# evenodd(10.5)
# evenodd(11)
# evenodd(12)


# def factorial(n):
#     result=1
#     while n>=1:
#         result= result *n
#         n=n-1
#     return result

# for fact in range(1, 6):
#     print("The factorial of {} is {}".format(fact,factorial(fact)))



# def wish(name , msg):
#     print("HELLO", name , msg)


# wish(name="Krishna" , msg="How r u?")

# wish(msg="GOOD MORNING", "KRISHNA")





# def wish(name="Guest"):
#     print("Hello" , name, "Good Evening")

# wish("krishna")
# wish()





# def sum(*n):
#     result=0
#     for x in n:
#         result= result + x
#     return result

# print(sum(10))
# print(sum())
# print(sum(10,20,30))



# def sum(name,*n):
#     result=0
#     for x in n:
#         result= result + x
#     print("The sum of",name , "is: ", result)

# (sum("RAVI",10,20,30,40))
# # (sum("Krishna"))
# (sum("TINNY"  ,10,20,30 ))



#kwargs

# def display(**kwargs):
#     print("RECORDS:")
#     for k,v in kwargs.items():
#         print(k,":",v)
#     print()
    


# display(name="krishna" , age=19, gf="none" , wife="none")
# display(name="trisha" , age=21, bf="none" , husband="applicable")


#global and local variable 

# a=10
# def f1():
#     # global a                          #will globalise a=777 so a=10 will replace by a=777 and that a=777 will available to other functions as well. 
#     a=777 
#     print("a: ",a)                     #gives a=777
#     print(globals()['a'])                   #gives a=10 

# def f2():
#     print("a: ",a)


# f1()
# f2()




#Recursive function


# def factorial(n):
#     if n == 0:
#         result =1
#     else:
#         result=n*factorial(n-1) 
#     return result

# print(factorial(5))






#Anonymous Function


# s=lambda n:n*n
# print(s(4))





#filter()

# WITHOUT LAMBDA
# def iseven(n):
#     if n%2==0:
#         return True
#     else:
#         return False
    
# l=[0,5,10,20,25,30]
# l1=filter(iseven,l)
# # print(l1)-----------------------> <filter object at 0x000001425C0BB8B0>

# l1=list(filter(iseven,l))
# # print(l1) -------------------------> [0, 10, 20, 30] all even numbers




#Filter() WITH LAMBDA


# l=[0,5,10,15,20,25,30]

# l1=list(filter(lambda x:x%2==0, l))

# print(l1)





#map()  WITHOUT LAMBDA


# def double(x):
#     return 2*x
# l=[0,5,10,20,25,30]
# l2=map(double,l)
# # print(l2) ---------------------->   <map object at 0x00000218102DB7C0>

# l2=list(map(double,l))
# # print(l2) ------------------------>    [0, 10, 20, 40, 50, 60] all numbers are doubled and the input values and output values are same 




#map()  WITH LAMBDA

# l=[0,5,10,15,20,25,30]
# l1=list(map(lambda x:2*x, l))
# print(l1) ---------------------------->  [0, 10, 20, 30, 40, 50, 60] 




#NOTE: We can apply map() function on multiple sequences , if both sequence contain same number of elements, if sequence is not same then extra numbers will be ignored --> no error generated

# example:

# l1=[1,2,3,4,5]
# l2=[10,20,30,40,50]

# l3=list(map(lambda x,y: x*y , l1,l2))
# print(l3)

# print(l3) --------------------------------->  [10, 40, 90, 160]




#reduce() fuction

# from functools import reduce

# l=[10,20,30,40,50]

# result=reduce(lambda x,y:x+y , l)
# print(result) 





#function aliasing

# def wish(name):
#     print("GOOD MORNING",name)

# greet=wish
# wish("KRISHNA")
# greet("DURGA")

# del greet

# wish("XYZ")
# greet("KRISHNA AND DURGA") ----------------->  NameError: name 'greet' is not defined





#NESTED FUNCTIONS


# def outer():
#     print("Outer functions executed...")
#     def inner():
#         print("Inner function executed...")
#     inner()

# outer()







#NOTE : How to access inner function outside of function

# def outer():
#     print("OUTER FUNCTION EXECUTED....")
#     def inner():
#         print("INNER FUNCTION EXECUTED...!")
#     return inner

# f1=outer() --------->  Since outer function returning inner fuction so now f1 carrying inner function

# f1()---------------> Therefore this will directly call inner function --> INNER FUNCTION EXECUTED...!




#DECORATORS

# def decorator(func):
#     def inner(name):
#         if name=="XYZ":
#             print("HELLO XYZ BAD MORNING")
#         else:
#             func(name)
#     return inner



# @decorator-------------------------------> use this if you only want extended funxtionality
# def wish(name):
#     print("HELLO GOOD MORNING", name)

# decorFunction = decorator(wish)----------> Extended functionality is added in decorFunction. Now using decorFunction we can use extended functionality and just by using wish() we can use normal function.

# decorFunction("XYZ")
# wish("XYZ")




#EXAMPLE-2

# def smartDivision(func):
#     def inner(a,b):
#         if b==0:
#             print("Can't divide by zero...!")
#         else:
#             return func(a,b)
#     return inner   


# @smartDivision
# def division(a,b):
#     return a/b


# print(division(10,5))
# print(division(10,0))


#NOTE: multiple decorator can be applied to single function


# def decor(func):
#     def inner(name):
#         print("First decor function executed...")
#         func(name)
#     return inner

# def decor2(func):
#     def inner(name):
#         print("Second decor executed....")
#         func(name)
#     return inner 


# @decor
# @decor2
# def wish(name):
#     print("Hello good morning", name)


# wish("durga")

#----------------------------------------------------------------


def decor1(func):
    def inner():
        x=func()
        print("EXUECUTED DECOR-1")
        return x*x
    return inner

def decor2(func):
    def inner():
        x=func()
        print("EXUECUTED DECOR-2")
        return 2*x
    return inner

@decor1
@decor1
def num():
    return 10

print(num())



# l=(x*x for x in range(10000000000000000))
# for x in l:
#     print(x)



# def decor(wish):
#     def inner(name):
#         if name == "Sunny":
#             print("BAD MORNING SUNNY...!")
#         else:
#             wish(name)
#     return inner

# @decor
# def wish(name):
#     print("HELLO GOOD MORNING", name)


# wish("Krishna")
# wish("Sunny")