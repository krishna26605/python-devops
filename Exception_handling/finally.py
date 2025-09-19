def try_error():
    try:
        l = [1 , 2 , 3 , 4 , 5 , 6]
        i = int(input ("enter the number :"))
        print(l[i])
        return 1

    except:
        print("Some error occured ..")

        return 0

    finally:
        print("Always get executed")
    # print("Always executed..")

x= try_error()
print(x)