# f=open('abc.txt','r+')

# print("FILE NAME : ", f.name)
# print("FILE MODE : ", f.mode)
# print("FILE Closed?? : ", f.closed)
# print("IS FILE READABLE?? : ", f.readable())
# print("IS FILE WRITABLE?? : ", f.writable())

# f.close()
# print("FILE Closed?? : ", f.closed)



#WRITING DATA TO TEXT FILES :

f= open('test.txt','w')

f.write("Hello\n")
f.write("Krishna\n")
f.write("Good\n")
f.write("Morning\n")

f.writelines(["Hey how are you??"])
f.close()

print("Writing to file done successfully...")