# import keyword

# print(keyword.kwlist)

# x = [10, 20 , 30 , 40]
# b= bytearray(x)
# b[0]= 25

# print(type(b))
# for element in b:   
#     print(element)


# l=[]
# l.append(10)
# l.append(20)
# l.append(90)
# l.append(30)
# l.append(40)
# l.append(50)

# print(l[1:5])
# print(l)

# s = ("krishna", 34, 88)
# s= s*2
# print(type(s))


# r =range(10)
# for ele in r:
#     print(ele)

# print(r[4])


# for i in range(10, 50 , 2):
#     print(i)

# s = {11}
# for i in range(0 , 10):
#     s.add(i)

# print(s)

# d = {}

# print(type(d))

# d = {}

# d["name"] = "Krishna"
# d["name"] = "Nikam"
# print(d)

# l = [23, 45    , 34]
# b= bytes(l)
# print(type(b))
# print(l)

# x = [12, 34 , 24]
# b = bytes(x)
# print(x)

# a = "durga"
# b = "Durga"
# print(id(a))
# print(id(b))

# print(a is b)
# list = [10, 20 , 23, 40]
# s = "Hello how are you??"
# # print(9 or 22 in list)
# print("" in s)


# import math

# # print(math.sqrt(16))
# print(math.sin(0))


# from math import pi

# r = int (input("Enter RADIUS:"))
# AREA = pi*r**2
# print("Area of circle is : ", AREA)

# a,b,c,d=[int(x)for x in input("Enter 4 values").split(',')]
# print("a = ",a)
# print("b = ",b)
# print("c = ",c)
# print("d = ",d)


# x = eval(input("Enter some data: "))
# print(type(x))


# a, b, c =[eval(x) for x in input("Enter three values: ").split(",")]
# print(type(a))
# print(type(b))
# print(type(c))


# from sys import argv
# args = argv[1:]
# sum =0
# for x in args:
#     n=int(x)
#     sum = sum + n
# print("The sum is :" , sum)

# from sys import argv
# print(eval(argv[1])+ eval(argv[2]))

# name = "Durga"
# salary= 10000
# gf= None

# print("Hello {0} , your salary is {1} and your girlfriend {2} is waiting...".format(name, salary, gf))


# name = ""

# while name !="durga":
#     name=input("Enter name:")
# print("Hello Durga")





# for i in range(4):
#     for j in range(4):
#         print("i={} and j={}".format(i,j), end="" )



# n= int(input("Enter number:"))

# for i in range(1 , n+1):
#     for j in range(1,i+1):
#         print(" * ", end="")
#     print()


# n= int(input("Enter number:"))                    ///////LEC-19
# for i in range(1 , n+1): 
#     for j in range(1 , n+1):
#         print("*" , end=" ")
#     print()



# n= int(input("Enter number:"))  

# for i in range(n , 0 , -1):
#     for j in range(1 , i+1):
#         print("*", end=" ")
#     print()



# n= int(input("Enter number:"))  

# for i in range(n , 0 , -1):
#     print(" * " * i)


# Name = input("Enter a string : ")
# i=0
# for elem in Name:
#     print("The positive index {} and negative index {} present character is : {} ".format(i,i-len(Name),elem ))
#     i = i+1




# n = input("Enter a string: ")
# s=len(n)
# i=0
# print("DATA IN FORWORD DIRECTION...")
# while(i<s):
#         print(n[i] , end="")
#         i= i+1
        



# n = input("Enter a string: ")
# s=len(n)
# i=0
# print("DATA IN BACKWARD DIRECTION...")
# i = s-1
# while(i>=0):
#         print(n[i] , end="")
#         i= i-1
        

# string = input("Enter a string: ")
# subs = input("Enter the substring: ")

# try:
#     n=string.index(subs)
# except ValueError:
#     print("Something goes wrong...!")
# else:
#     print("Substring found at index {}".format(n))

# string = input("Enter a string: ")
# subs = input("Enter the substring: ")
# n = len(string)
# pos = -1
# flag = False
# count = 0
# while True:
#     pos=(string.find(subs, pos+1 , n))
#     if pos == -1:
#         break
#     print("FOUND AT INDEX {}".format(pos))
#     flag= True
#     count = count +1
# print("The total time argu occurs is " , count)
# if flag == False:
#     print("NOT FOUND.....!")


# s = "abababab"
# print(id(s))

# s=s.replace("a" , "b")

# print(id(s))

# print("avc1232".islower())

# print("   ".isspace())


# s = input("Enter the string:")
# i = len(s)-1
# output=""

# while i>=0:
#     output=output+s[i]
#     i=i-1
# print(output)


# s = input("Enter string: ")
# l=s.split()
# l2 = []
# i = len(l)-1

# while i>=0:
#     l2.append(l[i])
#     i=i-1
# output=" ".join(l2)
# print(output)/



# s = input("Enter string: ")
# l=s.split()
# l2 = []

# for ele in l:
#     l2.append(ele[ : :-1])
# print(l2)



# n = input("Enter String:")
# newStr= ""
# for ele in n:
#     if(ele in newStr):
#         pass
#     else:
#         newStr= newStr+ ele
# print(newStr)


