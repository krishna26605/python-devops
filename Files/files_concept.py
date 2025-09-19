#///////////////OPERATIONS ON FILES [OPEN READ & CLOSE] .///////////////////


# Reading  a File 
f = open("Files/demo.txt" , "r")
data =  f.read()
print(data)
print(type(data))
f.close()


# Wriring a File
#"w"-- overwrite file [deletes previous data and writenew data]
#"a"-- append mode it will append to file does not deletes data inside file

f= open("Files/demo.txt" , "w")
f.write("my name is krishna nikam 123")
f.close()


f= open("Files/demo.txt" , "a")
f.write("I'm trying to learn devops ")
f.close()

# Deleting Files we have to import os module 
# import os
# os.remove("Files/demo.txt")