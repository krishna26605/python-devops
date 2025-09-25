# WAP : To take dic from kryboard and print sum of values

# dic={}
# n= int(input("Enter the keys u want to give:"))
# i=1

# while i<=n:
#     k=input("Enter the key: ")
#     v=input("Enter the value: ")
#     dic[k]=v
#     i=i+1
# sum=0
# for k,v in dic.items():
#     sum= sum + int(v)
# print(sum)


# using in build function the same above program..

# d= eval(input("Enter a dictionary: "))

# n=sum(d.values())
# print(n)


#number of occurence

# n= input("Enter the word: ")
# d={}
# for x in n:
#     d[x]=d.get(x,0)+1
# print(d)



#vowel occurences 
# v={"a","e","i","o","u"}
# d={}
# n= input("Enter the word: ")
# count=0
# for elem in n:
#     if elem in v:
#         d[elem]= d.get(elem,0)+1

# for k,v in d.items():
#     print("The vowels is {} and count is {}".format(k,v))        

    




# d={}
# n= int(input("Enter the number of students: "))
# i=1
# while i<=n:
#     name=input("Enter student name: ")
#     marks= int(input("Enter student marks: "))
#     d[name]=marks
#     i=i+1
# print(d)

# while True:
#     nameinput=input("Enter student name to know marks: ")
#     marks1= d.get(nameinput, -1)
#     if marks1==-1:
#         print("Student Not Found...")
#     else:
#         print("the marks of {} are {}".format(nameinput, marks1))

#     option= input("Do u want another student marks, [y/n]: ")
#     if option=="n":
#         break

# print("THANKS .........")

