
# //////////////////////// 1-100 ///////////
i =1 
while(i<=100):
    print(i)
    i= i+1


#/////////////////////////  100 -1 /////////////

i=100
while(i>=1):
    print(i)
    i= i-1


#////////////// MULTIPLICATION TABLE /////////


n= int(input("enter a number "))
i=1
while(i<=10):
    print(n*i)
    i = i+1


#//////////// printing list using loop //////////

l1 = [1 , 4 , 9, 36 ,3 , 6, 32, 73, 3]
idx = 0

while(idx<len(l1)):
    print(l1[idx])
    idx = idx + 1



#//////////////// Searching for a number in tuple ///////////


l1 = (1 , 4 , 9, 36 ,3 , 6, 32, 73, 3)
x=6
i = 0 
while (i<len(l1)):
    if(l1[i]==x):
        print("Element found at index " , i)
    i= i+1


#/////////////////////   BREAK ///////////////////////////

i = 1 
while (i<=5):
    print(i)
    if (i==3):
        break
    i += 1



#///////////////////////// CONTINUE ./////////////////////////

i = 1 
while (i<=5):
    if( i ==3):
        i += 1
        continue
    print(i)
    i +=1

