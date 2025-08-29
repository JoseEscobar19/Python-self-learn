len("Hello")

#subscripting
print("Hello"[2])

#Integers
print(123 + 456)

#large integers
print(123_456_789)

#floats
print(3.14567)

#Booleans
print(True)

print(False)
#////////////////////////////////////////////////////////////////////////////
#the below example wont work because len() only works with strings
#len(12345)

print(type(123))

print(type("123"))

print(type(1.23))

print(type(True))

#to convert a piece of data into a different data type - called type conversion or type casting in python
#sometimes the danger of this is you cant convert some things into a different data type
#for example if you tried int("abc") <- this would cause an error a valueError because how would you convert letters to num

int("123")

print(int("123")+ int("456"))
#the above is treated as integer values when using the int() function

#you can convert to all 4 data types

int()
float()
str()
bool()

print("Number of letters in your name: " , len(input("Enter your name")))

#the way recommended is to convert len() function to a string output

print("Number of letters in your name: " + str(len(input("Enter your name"))))

#////////////////////////////////////////////////////////////////////////////

print("My age: " + str(12))

#this gives you a return of a floating point even if it returns a whole number integer
print(6 /3)

#this below gives you the whole integer and removes any floating point using //
print(6 // 3)

#using two ** is an exponential
print(2 ** 3)

#////////////////////////////////////////////////////////////


