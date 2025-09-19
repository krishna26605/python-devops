
# ///////////////////////// AVG CALCULATOR ..///////////////////////////////
def Avg_No(a,b,c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg

Avg_No(2 ,3 ,4)

#//////////////// USD TO INR ///////////////////////////////////


def converter(USD):
    INR = USD * 83
    print(USD ,"USD =  " , INR , "INR")


converter(2)

#////////////////////// Function for odd even /////////////////////////////

def oddeven(number):
    if (number %2 == 0):
        print(" EVEN")
    else:
        print("ODD")


oddeven(5)



#///////////////////////////////  RECURSION /////////////////////////////////////////

#recursive function

def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)

show(5)


# /////////////////// FACTORIAL USING RECURSION /////////////////

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n


print(fact(3))