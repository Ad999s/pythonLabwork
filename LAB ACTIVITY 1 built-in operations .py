

str="hello"




str1="world"

#'id' function:

#This function returns the identity of an object. A identity has to be unique and constant for a particular object during the lifetime.
#Syntax : id(object)


print(id(str))



print(id(str)==id(str1))




#'type' function

#This function returns the data type of an object. It returns the following data types :
#1. Integer
#2. String
#3. Float
#type() method returns class type of the argument(object) passed as parameter. type() function is mostly used for debugging purposes.

#Syntax : type(object)


class dictype:
    dicnumber={1:'apple', 2:'kiwi', 3:'banana', 4:'guava'}
    print(type(dicnumber))





str1="hello"
a=20.5
b=10
print(type(str1))
print(type(a))
print(type(b))






