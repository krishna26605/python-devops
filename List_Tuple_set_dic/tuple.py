tup = (1 , 3 , "shoeb")
print(type(tup))
print(tup)



#/////////////  METHODS IN TUPLE ////////////////////


tup = (2 , 1 , 3, 1)
print(tup.index(1))                            # this will give first (occurence) time 1 kab aaya konse index pe aaya this will return index number

print(tup.count(1))                            # kitni baar 1 tuple me aaya he wo deta hai yaha pe 2 baar aaya hai to output 2 hai



#///////////////////////  QUESTIONS ///////////////////////////////

movies = []
movie01 = input("Enter your 1st fav movie : ")
movie02 = input("Enter your 2nd fav movie : ")
movie03 = input("Enter your 3rd fav movie : ")

movies.append(movie01)
movies.append(movie02)
movies.append(movie03)

print(movies)
print(type(movies))


