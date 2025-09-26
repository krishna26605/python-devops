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


s=lambda n:n*n
print(s(4))