# collection = {1 , 3 ,24, 3 , "hello" , "world"}
# print(collection)


#////////////////////////////////// SETS METHODS ////////////////////////


# NOTE :   set is mutable but the elements of set is immutable


collection = set()                  #empty set
collection.add(1)                   # add element in set 
collection.add(2)
collection.add(7)
collection.add("hello")
collection.add("krishna")
collection.remove(2)                # remove element from set 
print(len(collection))              # print length of set
# collection.clear()                # set become khalii
print(collection)           
print(collection.pop())             # remove any random element from set
print(collection) 


set1 = {1 , 2 ,3 , 4}
set2 = {2 ,3 , 4, 5 , 6 }

print(set1.union(set2))             # uninon of two set & it will return new set and does not change original set

print(set1.intersection(set2))      # return comman value in both the set