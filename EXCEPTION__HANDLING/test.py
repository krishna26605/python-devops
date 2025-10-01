# print("Hello started...")
# try:
#     print(10/0)
# except BaseException:                              # we can use ZeroDivionError as well
#     print(10/2)


# print("Ended....")


# HOW TO PRINT EXCEPTION INFORMATION

# try:
#     print(10/0)
# except ZeroDivisionError as msg:
    # print("We got an exception", msg) ------------------>  .We got an exception division by zero





#TRY WITH MULTIPLE EXCEPT BLOCK


# try:
#     x= int(input("ENTER THE VALUE OF X: "))
#     y= int(input("ENTER THE VALUE OF Y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Please provide valid int value")


#SINGLE EXCEPT CAN HANDLE MULTIPLE EXCEPTION



# try:
#     x= int(input("ENTER THE VALUE OF X: "))
#     y= int(input("ENTER THE VALUE OF Y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("cant divide by zero")
# except:                        ------------------------->  default 'except:' must be last
#     print("Provide valid inputs..")


# FINALLLY BLOCK


# import os
# try:
#     print("TRY")
#     os._exit(0)          ----------------->  Python virtual machine explicitly shutdown , this is the only case when finally block will not execute
# except ValueError:
#     print("EXCEPT")
# finally:
#     print("FINALLY")

 
# ---------------------------------------------------------
#PRACTICE
# n= int(input("Enter the number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
# ---------------------------------------------------------------



