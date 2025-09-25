# dict={}
# n= int(input("Enter the number of students:"))
# i=1
# while i<=n:
#     name=input("Enter the student name: ")
#     marks=input("Enter the student marks: ")
#     dict[name]=marks
#     i=i+1
# print(dict)



# s= {1, 2, 3,4, 5,6}
# l={"name":"Krishna", 100:"durga"}
# s.update(l.values())
# print(s)




# s= {1, 2, 3,4, 5,6}
# l=11
# s.add(l)
# print(s)
# s.pop()                # In set pop method does not take any arguments..
#                         # But in list pop method can take index as an argument..
# print(s)






# s1 = {12,23, 45, 56, 74}
# s2 ={ (12,34,55), "krishna" , "durga" , 12}

# p=(s1.union(s2))
# print(p)

# print(s1.intersection(s2))

# print(s2.difference(s1))      #present in s2 but not in s1


# print(s1.symmetric_difference(s2))  # present in s1 not in s2 & present in s2 not in s1 --- common elements in both discarded




#SET COMPREHENSION

# s= { i*i for i in range(1,11)}

# print(s)


# s2= { i for i in s if i%2==0}

# print(s2)