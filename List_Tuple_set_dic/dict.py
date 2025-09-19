
# #///////////////////////////     DICTIONARIES  ////////////////////////////


info = {
    "name" : "krishna" , 
    "percenatge" : 99.900 ,
    "subjects" : ["math" , "phy" , "chem"] ,
    "topics" : ("set" , "dict"),
    "age" : 90 ,
    "is_adult" : True ,
    12 : 69

}

print(type(info))
print(info["name"])
info["name"] = "kishuu"
info["surname"] = " nikam"
print(info)


#///////////////////////////////////////////// NESTED DICT /////////////////////////////////////////

Students = {
    "name " : " rahul kumar" ,
    "subjects" : {
        "math" : 90.98,
        "phy" : "failed",
        "chem" : 78.0
    }
}

print(Students["subjects"]["math"])




#//////////////////////////// DICT METHODS ///////////////////////////////


Students = {
    "name" : " rahul kumar" ,
    "subjects" : {
        "math" : 90.98,
        "phy" : "failed",
        "chem" : 78.0
    }
}
print(Students.keys())                              # .key method return all the keys in dictionary
print(Students["subjects"].keys())


print(Students.values())                           # .value method returns all values in dict

print(list(Students.items()))                      # return all key value pair in the form of tuple

print(Students.get("name"))                        # print name but if i gave wrong key it will show output as None 
print(Students["name"])                            # print name but if i gave wrong key then it will show error 



Students.update({"city" : "Nashik"})
print(Students)

