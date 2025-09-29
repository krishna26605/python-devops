# import krishnamath
# krishnamath.add(10,20)

    #  OR 

# from krishnamath import *   --------------------- >  In this syntax no need to use krishnamath.add(), directly can use add(20,10)
# add(20,10)
 
        # OR

# import krishnamath as km    (Aliasing)  --------------------- >  In this syntax you need to use km.add(),  km.add(20,10)
# km.add(20,10)

#NOTE: we can alias module name as well as members of module also we can create alise name

# from krishnamath import add as a, sub as s , product as p
# a(10,20)
# s(20,10)
# p(10,20)



# import krishnamath
# import time
# import math
# from importlib import reload

# time.sleep(15)
# reload(krishnamath)
# import krishnamath
# print("This is last line of code...")

# print(dir(math))


# print(__doc__)
# print(__loader__)
# print(__name__)
# print(__package__)
# print(__spec__)
# print(__cached__)
# print(__file__)
# print(__builtins__)
# print(__package__)
# print(__dict__)
# print(__annotations__)
# print(__path__)

# import math

# help(math)



from random import *

# for i in range(10):
#     print(random())        -----------> exclusive random() always give float value between 0 and 1 and 0 and 1 is exclusive


# for i in range(10):
#     print(randint(1,100))  ------> randint() give int value in 1,100 inclusive 1 and 100



# for i in range(10):
#     print(uniform(1,10))  --------> uniform() give float value between 1,10 exclusive 1 and 10

# l=["krishna","durga","sunny","bunny"]
# for i in range(10):
#     print(choice(l))



# WAP : six digit otp

# for i in range(6):
#     print(randint(0,9), end="")


#WAP: 1,3,5--alphabets and 2,4,6 digits


# for i in range(6):
#     print(chr(randint(65,65+25)), randint(0,9) , chr(randint(65,65+25)), randint(0,9), chr(randint(65,65+25)),randint(0,9) , sep="")