#///// printing list using for loop //////////////////

l1 = [1 , 4 , 9, 36 ,3 , 6, 32, 73, 3]

for i in l1:
    print(i)


#/////////////////// RANGE /////////////////////////////


seq = range(5)
for i in seq:
    print(i)


for i in range(1 , 10 , 2):          #range(start , stop , stepsize)
    print(i)



#///////////////// FACTORIAL OF NATURAL NUMBER .//////////////////////////////// USING WHILE LOOP

n = 3
fact = 1
i = 1
while (i<=n):
    fact = fact * i
    i = i +1

print("factorial is " , fact)









#/////////////////////   FACTORIAL USING FOR LOOP /////////////////////////////////
n = 3
fact = 1
i = 1
for i in range( 1 ,n+1):
    fact= fact * i 
    i = i+1
print("factorial is " , fact)
