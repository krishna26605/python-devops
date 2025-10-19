#REVERSE A STRING

# s="Krishna"
# i=len(s)-1
# while i>=0:
#     print(s[i], end="")
#     i=i-1


# Check if a string is a palindrome


# s=input("Enter a String: ")
# i=0
# n=len(s)-1

# while i<n:
#     if s[i]==s[n]:
#         i=i+1
#         n=n-1
        
#     else:
#         print("not a palindrome")
#         break
# else:
#     print("Its a palindrome")

          # or 


# s= input("Enter a string: ")
# if s==s[: : -1]:
#     print("Palindrome")
# else:
#     print("not a palindrome")



# Count the number of vowels in a string

# s= input("Enter a string: ")
# vowels = ["a", "e", "i", "o", "u"]
# count=0
# for elem in vowels:
#     if elem in s:
#         count= count+1
# print("String contains {} vowels".format(count))    




# n= input("Enter input: ")
# list=[]
# for elem in n:
#     if elem not in list:
#         list.append(elem)
#     else:
#         pass 
# print("".join(list))




# n=input("Enter input: ")
# output=""
# for elem in n:
#     if elem.isalpha():
#         output=output+elem
#         prev=elem
#     else:
#         output=output+ prev * (int(elem)-1)
# print(output)





# n= input("Enter input")
# output=""
# for elem in n:
#     if elem.isalpha():
#         output=output+elem
#         prev=elem
#     else:
#         newchr= chr(ord(prev)+int(elem))
#         output=output+newchr
# print(output)




# s1= input("Enter input: ")
# s2= input("Enter input: ")

# i=0
# j=0
# output=""
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         output=output+s1[i]
#         i=i+1
#     if j<len(s2):
#         output=output+s2[j]
#         j=j+1
# print(output)
