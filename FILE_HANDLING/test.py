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

# data = "ALL STUDENTS ARE STUPIDS"
# f= open('test.txt', 'w')
# f.write(data)

# with open('test.txt', 'r+')as f:
#     list=f.read()
#     print(list)
#     print("The current cursor position is: ", f.tell())
#     f.seek(17)     #------------------> Jumps to 17th position 
#     f.write("GEMS...!") # -----------------> Override the STUPIDS with GEMS 
#     f.seek(0)  # ----------------------> then again jumps to zero position
#     list=f.read()  # ------------------> from pointer at zero therefore read all data 
#     print("DATA AFTER MODIFICATIONS..")
#     print(list)            #---------------> print the modified data 





# WAP : TO FIND NO. OF LINE , WORD , CHARACTER PRESENT IN A LINE 
# import os
# fname= input("Enter a file name: ")
# if os.path.isfile(fname):
#     print("File Exist,",fname)
#     f=open(fname, 'r')
# else:
#     print("File does not exixt with name",fname)

# lcount=wcount=ccount=0

# for l in f:
#     lcount=lcount+1
#     ccount=ccount+len(l)
#     words= l.split()
#     wcount=wcount+len(words)

# print("The line count is:", lcount)
# print("The word count is:", wcount)
# print("The character count is:", ccount)






#PROGRAM TO COPY BINARY FILE 

# HANDLING BINARY FILES:

# f1=open("p-maharaj.jpg",'rb')
# f2=open('new-p-maharaj.png','wb')

# bytes=f1.read()
# f2.write(bytes)

# print("The new file is new-p-maharaj")

# -------------------------------------------------------------


# f1=open("p-maharaj.jpg",'rb')
# f2=open('new-p-maharaj.jpg','wb')

# bytes=f1.read()
# f2.write(bytes)

# print("The new file is new-p-maharaj")





#HANDLING CSV FILES: USING CSV MODULE 

# WRITING DATA TO CSV FILE:
# import os,csv

# with open("emoplyeedata.csv", 'w', newline='') as f:
#     w=csv.writer(f)
#     w.writerow(["EmployeeNumber", "EmployeeName","EmployeeSalary", "EmployeeAdddress"])
#     n=int(input("Enter the Number of employees: "))
#     for i in range(n):
#         enumber=int(input("Enter EmployeeNumber: "))
#         ename=input("Enter Employeename: ")
#         esal=float(input("Enter EmployeeSalary: "))
#         eaddr=input("Enter EmployeeAddress: ")
#         w.writerow([enumber,ename,esal,eaddr])

# print("CSV file written successfully...")


#READING DATA FROM CSV FILE:
# import csv
# f=open('emoplyeedata.csv', 'r')
# r=csv.reader(f)
# data=list(r)
# for line in data:
#     for word in line:
#         print(word , '\t', end='')
#     print()








#ZIPPING AND UNZIPPING



# Zipping data done...
# from zipfile import *

# f=ZipFile("files.zip","w",ZIP_DEFLATED)
# f.write("cricketers.txt")
# f.write("timepass.txt")
# f.write("heros.txt")
# print("Zipping file done successfully..")
# f.close()




# Unzipping data ....

# from zipfile import *

# f=ZipFile("files.zip",'r', ZIP_STORED)
# names = f.namelist()
# for name in names:
#     print("Files name: ", name)
#     print("The Content of File is :")
#     f=open(name , "r")
#     print(f.read())
#     print()




# WORKING WITH DIRECTORIES

# import os
# currentDirectory= os.getcwd()
# print(currentDirectory)    #------------------->  C:\Users\Krishna\OneDrive\Desktop\PYTHON-FULL\FILE_HANDLING




# import os 
# os.system("notepad")




import os 
from datetime import *
stat= os.stat("test.py")
print(stat)  #---------------------->  os.stat_result(st_mode=33206, st_ino=313000174102260714, st_dev=9847744664029331884, st_nlink=1, st_uid=0, st_gid=0, st_size=5280, st_atime=1759594322, st_mtime=1759594321, st_ctime=1759422397)
print("The file size in bytes is : ", stat.st_size)
print("The file last access time is : ", datetime.fromtimestamp(stat.st_atime))
print("The file last modified time is : ", datetime.fromtimestamp(stat.st_mtime))
# print("The file last access time is : ", datetime.fromtimestamp(stat.st_atime))



# import datetime

# print(dir(datetime))