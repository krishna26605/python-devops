marks = [23.3 , 44.3 , 22.2 , 56.3 , 43.4 , 89.3 , 99.9]
print(marks)
print(type(marks))
print(marks[0])
print(marks)       # List is mutable / can change 


marks[0] = 56.666          # we have change first number with the help of index number in list
print(marks)


#//////////////////////////////////  LIST METHODS .///////////////////////////////////////


# / NOTE :   list update original list it will not create new list hence by printing list it returns NONE

list = [2 , 1 , 3 , 1]
list.append(4)                           # add 4 at the last of list 
list.sort()                              # sort it in ascending (from smaller to greater)
list.sort(reverse=True)                  # sort in descending (from greater to smaller)
list.reverse()                           # reverse the string 
list.insert(1 , "andiii")                # insert element at given index
list.remove(1)                           # it will remove first occurence of number 
list.pop(3)                              # it will remove element by index number here it will remove 1 which is at 3rd index 
print(list)



#////////////////////////  palindrome = saamne se piche se same hai ///////////////////////////////


list1 = [1,2,2,3]
cp_list = list1.copy()
cp_list.reverse()
if (cp_list==list1):
    print("this is palindrome list")
else:
    print("not a palindrome")