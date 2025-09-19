n = int(input("enter number between 3 and 8 :"))
if(n>8 or n<3):
    raise ValueError("Value entered is incorrect")
else:
    print(f'the number you have entered is {n}.')