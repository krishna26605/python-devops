# f=open('abc.txt','r+')

# print("FILE NAME : ", f.name)
# print("FILE MODE : ", f.mode)
# print("FILE Closed?? : ", f.closed)
# print("IS FILE READABLE?? : ", f.readable())
# print("IS FILE WRITABLE?? : ", f.writable())

# f.close()
# print("FILE Closed?? : ", f.closed)



#WRITING DATA TO TEXT FILES :

# f= open('test.txt','w')

# f.write("Hello\n")
# f.write("Krishna\n")
# f.write("Good\n")
# f.write("Morning\n")

# f.writelines(["Hey how are you??"])
# f.close()

# print("Writing to file done successfully...")





# Reading character data from file 


# f= open('test.txt' , 'r')
# # data=f.read()   #--------------------------> Read all the data from file 
# # data = f.read(10)  #------------------------------> Read only first 10 characters 
# print(f.readline())  # ------------------------------> Read only one line   -->  Hello
# print(f.readline())   # ---------------------------> Read second line -->  Krishna
# f.close()


# f= open('test.txt' , 'r')
# list=f.readlines() #      ------------- > [read file in list ]
# print(list) # ---------------->  ['Hello\n', 'Krishna\n', 'Good\n', 'Morning\n', 'Hey how are you??']




# f= open('test.txt' , 'r')
# list=f.readlines()
# for l in list:
#     print(l , end="")
# f.close()



#with statement


# with open('test.txt', 'r') as f:
#     data= f.read()
#     print(data)
#     print("Is file closed?: ", f.closed)   #-------> False

# print("Is file closed?: ", f.closed)      # ----------> True




#tell()    ---------------------------> tells current pointer position/ index

# f= open('test.txt','r')
# print(f.tell())  # ----------> 0 pointer at begining
# print(f.read(4))
# print(f.tell())  #  -----------> 4 pointer at 4th index
# print(f.read(4))
# print(f.tell())  #-----------> 9 pointer at 9th index





# seek()



data = "ALL STUDENTS ARE STUPIDS"
f= open('test.txt', 'w')
f.write(data)

with open('test.txt', 'r+')as f:
    list=f.read()
    print(list)
    print("The current cursor position is: ", f.tell())
    f.seek(17)     #------------------> Jumps to 17th position 
    f.write("GEMS...!") # -----------------> Override the STUPIDS with GEMS 
    f.seek(0)  # ----------------------> then again jumps to zero position
    list=f.read()  # ------------------> from pointer at zero therefore read all data 
    print("DATA AFTER MODIFICATIONS..")
    print(list)            #---------------> print the modified data 