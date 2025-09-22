# list

# list=["A" , "B" , "C" , "D" , "E" , "F"]
# n= len(list)
# for elem in range(n):
#     print(list[elem], "The positive index is {} and negative index is {}".format(elem,elem-n))
    

# l=[]
# for elem in range(101):
#     if elem%10==0:
#         l.append(elem)
# print(l)




# list=[[1,2,3],[4,5,6],[7,8,9]]
# print("ROW WISE...")
# for elem in list:
#     print(elem)

# print("MATRIX WISE...")
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         print(list[i][j], end=" ")
#     print()



# list=[]
# for elem in range(1,11):
#     list.append(elem*elem)
# print(list)


# l1= [elem*elem for elem in range(1,11)]            #square number from 1-10  #LIST COMPREHENSIONS..
# l2=[elem for elem in l1 if elem%2==0]              #even number from that squares of 1-10
# print("LIST 1 :" , l1)
# print("LIST 2 :" , l2)


# string= "the quick brown fox jumps over the lazy dog".split()
# # print(string)

# l2= [w.swapcase() for w in string]
# print(" ".join(l2))



# n= input("Enter a string: ")
# s=len(n)
# vowels=["a","e","i","o","u"]
# found=[]
# for letter in n:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# print(found)


