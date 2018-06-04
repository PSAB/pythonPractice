# -*- coding: utf-8 -*-
# from __future__ import print_function, absolute_import, division


sampleString = "Hey there"
print("Look at the following greeting: %s along with this: %s" %(sampleString, 420))

sampleArray = [num * 2 for num in range(1, 5)]
print(sampleArray)


# Now starting floating point number practice:
print("Lets get started with this: %5.3f" %(34.56632113)) #34.566

#Using the string.format method
print("The following value is positive: {a}, negative: {b}, and neutral: {c}".format(a = 1, b = str(-1), c = 0))

print("This number repeats itself twice: {a} and {a}, along with this: {b}".format(a = 1, b = 5))


# Moving on to lists

#You can concatenate lists:
sampleArray = sampleArray + [9, 10, "fourteen"]
print(str(sampleArray) + "\n")
print(sampleArray * 2) #outputs the entire sequence twice

# In python 3, division operation outputs a float
print(25/5)
# A double slash used in division outputs a truncated int result
print(25//3)

int("250") #250 int value

str(45.6) # String value of 45.6

# plaving an r in front of a string enables the backslash to be printed rather than be recognized as an escape character
print(r"this backslash \t is so good OMG")

# methods that apply to sequences apply to strings since strings are recognized as a sequence
# But in addition to sequence methods, there are also methods that work specifically on strings

sampleString = "I am so cool"
upperVersion = sampleString.upper() # I AM SO COOL
print(upperVersion)
replaceString = sampleString.replace("cool", "lame")
print(replaceString)


# the find method for strings finds substrings
singer = "Michael Jackson"
locationNum = singer.find("Jack")
print(locationNum)

print(singer.replace("Jackson", "Jordan"), "is cooler")

# Now here is practice with tuples
tuple1 = ("disco", "backsass", 3, 4, 6, 2, 5454, 6564, 43)
print(type(tuple1)) # Every tuple is of type 'tuple'

print("The second element of tuple1 is:", tuple1[1]) #tuple elements are accessed with brackets and are also sequences

# Remember that tupes are immutable just like Strings.
# We cannot modify tuples; our only other option is to create a new tuple:
tupleSorted = sorted(tuple1)
print(tupleSorted)

# Tuples can also contain other tuples as well, demonstrating nested structures.

tupleNest = (2, 5, 334, ('one', 'two', 'three'), 45, 567, 2342)
print(tupleNest[3][1]) # 'two'
print(tupleNest[3][2][2]) # 'r'

# For lists, I can use the 'extend' function to add a chunk to the end of an existing list.
print("This is the original sampleArray:", sampleArray)
sampleArray.extend([45, 2345, 6435, 'dfgfdre', 'look at me now'])
print("This is the new sampleArray", sampleArray)

print(tupleNest.index(2342))

newArray = sampleArray[:] # The array colon at the end is what actually copies the list rather than referencing the same value
print("newArray is:", newArray)
print("sampleArray is:", sampleArray)
del(sampleArray[0])
print("\n")
print("sampleArray is now:", sampleArray)
print("newArray is now:", newArray)



#To create a dicitonary, we use curly brackets

# Sets are also a type of collection, but they are unordered and they only have unique elements.
# To define a set, use curly brackets

set1 = {"toyota", "honda", "ford", "fiat", "lincoln", "bmw", "ferrari", "toyota", "honda", "lincoln", "ford", "ferrari", "fiat", "toyota"}
print(set1)
# Notice that when the set is printed, there is no duplicate of any of the objects

# You can convert a list to a set in a separate variable:
album_list = ['Michael Jackson', 'Thriller', 'Thriller', 1983]
album_set = set(album_list)
print("album_set is now:", album_set)

# The elements are now all unique

#The add method is used to add elements to a set
# Likewise, the remove method can be used to remove elements from a set

album_set.add('Eagles')
print(album_set)

# The in method can be used to check if a certain element is within a set

print('Eagles' in album_set) # Check if an element is in a set

# Using ampersand and intersection to only get items located in both sets:
car_set_1 = {"toyota", "honda", "ford", "hyundai", "gmc", "cadillac", "bmw", "audi"}
car_set_2 = {"hyundai", "cadillac", "mercedes", "bmw", "yugo", "kia", "ferrari"}
car_set_3 = car_set_1 & car_set_2
print(car_set_3)

# To check if a set is included as part of another set:
print("check the car subset:", car_set_3.issubset(car_set_1))
print("")
# We can use two straight lines to use union operation on sets:
#car_set_4 = car_set_1 || car_set_2
A=[1,2,2,1]
B=set([1,2,2,1])
print("the sum of A is:",sum(A))
print("the sum of B is:",sum(B))

print("makes only in car_set_1:", car_set_1.difference(car_set_2))

print("union of all cars:", car_set_1.union(car_set_2))

def add2(x):
    # The following is documentation for when help() is called on the function; You get to customize the message

    """
    add 2 to x
    :param x:
    :return:
    """

    y = x + 2
    print(y)

add2(45)
help(add2)

# The sorted(...) function returns a new data structure that is ordered, but the original data structure doesn’t change
# When the .sort() function is used, the original list will change and no new list will be created

def printSequence(sequence):
    for i, thing in enumerate(sequence):
        print(thing, "position at:", i)

# The multiplication symbol can also mean repeat a sequence
print(2 * 'Michael Jackson ')


# Python doesn't allow a function to have an empty body, so the keyword 'pass' can be used in place of an empty body
# IF no return statement is present, python automatically return a none
def noWork():
    pass

print(noWork())

car_list = ["toyota", "honda", "ford", "hyundai", "gmc", "cadillac", "bmw", "audi"]

def orderSequence(sequence):
    print("Before ordering:", end='')
    printSequence(sequence)
    sequence.sort()
    print("After ordering:", end='')
    printSequence(sequence)




orderSequence(car_list)
print("\n\n")

def pinkFloyd():
    global claimedSales # You can also manually delare variables to be within the global scope
    claimedSales = '45 million'
    return claimedSales

pinkFloyd()
print("accessed globally:", claimedSales) # No error due to global scope

# Every data type is a type of object in python
# For ex: Every time we create an integer, we create an instance of type integer

# Sorting is a built-in function of lists and other data structures, since lists are an object duh















