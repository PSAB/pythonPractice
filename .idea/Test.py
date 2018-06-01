#from __future__ import print_function, absolute_import, division
from datetime import datetime
#In python 3, print is a function not statement, so parentheses req. import below for python 3 printing only
#from __future__ import print_function

import time
import sys
import random
print (sys.platform) #darwin, so we're on a mac (Mac OSX Kernel name)
print(sys.version)
# A variable in Python takes on the type of value assigned
#lists are p much like indexed arrays in java, but they can grow and shrink ondemmand. Also heterogeneous to object types

#This is a list
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

print(datetime.today())

right_this_minute = datetime.today().minute

word = "bottles"
print(word)
#use the len function to print the length of a String.
print ("The length of the String 'word' is:", len(word))
print ("Printing the length of an explicit String:", len("ExplicitString"))

print("Hello")

print(3/2)  # ok good, we're on python 2

#powers
print(2**3)
#8
print(4**0.5)
#2.0

#Strings can also use single quotes apparently
singleQuoteString = 'hello'
doubleQuoteString = "Hey"

print ("You can use indexing right away: ", doubleQuoteString[0])
print ("Using indexing to access consecutive parts of a String sequence:", singleQuoteString[0 : len(singleQuoteString) - 1])

# The single quote can be used within this double-quoted string because that single quote would not
# be recognized as the ending of the String among the double quotes.
combineString = "Look at me, I'm flying"

# Both single and double quotes can be used in Python, but if your String happens to have an apostrpohe or something, you should
# use double quotes to escape that single quote.

print('Use newLine to create a new Line\n See what I mean? Looks like this is the same as in Java')

my_bool = True

# Creating a function within python
def printTwo():
    twoNum = 2
    return 2

print(printTwo())


s = "Hello World"
# from the second index onward
print (s[2:]) # llo World
# everything up to the third index
print (s[:4])
# INDEX OF -1 LOOPS AROUND ; everything except last letter
print (s[:-1], "is the result of s[:-1]")

# we can also use slice notation to separate elements of a sequence by a psecified STEP SIZE

# print every second letter of string
print (s[::2])

# print the entire String backwards
print (s[::-1])

# We cannot change the elements within a String once it is created, because it is immutable
# s[0] = 'R'  <----- This results in an error

# But we can still concatenate Strings
s = s + ' concatenate me'
print (s)

# Strings can also be multiplied to create repetition:
letter = 's'
print (letter * 10)

# STRING BUILT-IN METHODS
print (s.upper())
print (s.lower())

# The split method divides a String by spaces(default), and represents the String as a list
print (s.split()) # default is space
print (s.split('l')) # doesn't include the actual element that was split on
print (s.split('e'))

k = 'stringThing'
j = 'otherString'
firstInt = 9
# putting in values within a String: (s is for strings, d would be used for integers
print ('Place another String with a mod and s: %s' % (k) + ' and this: %s' % (j) + ' for the %d' % (firstInt) + 'th time')
print ('The two values being substituted in this String are this one: %s and this one: %s' % (k, j))
s2 = 'second'
s3 = 'PI'
d1 = 3.14
# in %3.1f, the 3 is the minimum # of digits long (including decmial point) of the String. 1 is how many after decimal point, rounding
# minimum # of digits leaves whitespace if longer than the quantity digit length, including decimal points.
print ("Let's do this for the %s time, we know %s is %10.3f"  % (s2, s3, d1))

# printing floating point numbers"
print ('Floating point numbers: %1.2f' % (1305.344))

# YOU can also format strings in print statements using the format method:
print ('Object 1: {a}, Object 2: {b}, Object 3: {c}' .format(a = 1, b = "two", c = 12.3))
print ('First: {a}, Second: {b}, Third: {c}' .format(a = 1, b = 2, c = 3.0))

#Like Strings, lists are also examples of sequences in Python. they can hold different object types
my_List = [1, 'two', 3.0, 1, 5]
print ('The length of this list is', len(my_List), 'units')
#Indexing and slicing also works similarly in lists
print ('my_list is', my_List)
#Concatenating a list:
my_List = my_List + [7.0]
print (my_List, 'concatenated by adding 7.0 to the end:')

print ('list multiplied by 2:', my_List * 2)

#Using the append method of lists:
my_List.append('eight')
print (my_List)

#Using the pop() method. By default it deletes the last index, but index can be specified in parameter
my_List.pop()
print (my_List)
my_List.pop(0)
print (my_List)

#Using the sort() method and the reverse() method
my_List.sort()
print (my_List)
my_List.reverse()
print (my_List)

# We can also use nested lists, kind of relateble to Java ain't it?
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, "nine"]
matrix = [list_1, list_2, list_3]

#Python Mappings, unlike sequences, store objects by keys instead of their positions. They don't retain order
# Dictionsries (A type of Mapping), contain a key and an associated value

# Making a dictionary with {} and : to signify the keys and values
my_dict = {'key1': 'value1', 'key2' : 'value2', 'key3' : "value3"}
#Call values by their key
print (my_dict['key2'])
my_dict['key2'] = 'The Amazing value2'
print (my_dict)

# We can also declare empty dictionaries and add keys by assignment
d = {}
d['animal'] = 'Dog'
d['answer'] = 42
print (d)  #{'answer': 42, 'animal': 'Dog'}

# Python is very flexible with nesting objects and directly calling methods on them
d2 = {'key': {'nestkey': {'subnestkey': 'value'}}}
print (d2['key']['nestkey']['subnestkey'])

#return a list of all the keys:
print (d.keys())
# return a list of all the values:
print (d.values())
# return a tuple of all items:
print (d.items())






#--------------------------------------------------------------------------
# s = 'STRING'
# print 'Place another string with a mod and s: %s' %(s)



# for i in range(5):
#     if right_this_minute in odds:
#         print("It is now an odd minute")
#     else:
#         print("It is now an even minute")
#
#     wait_time = random.randint(1, 60)
#     time.sleep(wait_time)





# for ch in "Hi!":
#     print(ch)
#
# for num in range(5):
#     print("Pythom rocks!")

# Dictionaries are a mapping, not a sequence like a list.
k = [1, 2, 3]
print (k[0])

my_dict = {'key1':'value1hhaaha', 'key2':'value2'}
print (my_dict['key1'])
print (matrix[2][2])

my_dict = {'key1':1, 'key2':'two', 'key3':78}
print (my_dict['key2'])
print ('tw' + my_dict['key2'][2] * 6)
print (my_dict['key2'][::-1].upper())

#empty dictionary to begin with
startEmpty = {}
#Then you can start manually adding keys and values
startEmpty['key1'] = 'dog'
startEmpty['key2'] = 'cat'
print (startEmpty)

# Prints only the keys of a dictionary
print (startEmpty.keys())

# Prints only the values of a dictionary
print (startEmpty.values())

# Prints out tuples of dictionary key and value pairs.
print (startEmpty.items())

# Constructing a tuple. Can create a tuple with multiple types
t = (1, 2, 3, 'four', 94)
print (len(t)) #3

#print t.index('fours')
print (t.count, "")

x = 'sample string'
print (x[::-1]) # print backwards
print (x.title())
t = "        baby      "
y =  x + t
print (y)
t.strip()
print (x + t.strip()) #get rid of whitespace


cars = ["bmw", 'audi', "toyota", "honda"]
cars.sort()
print (cars)
print("cars such as " + cars.pop(0) + " are too expensive")
print (cars)
cars.sort(reverse = True)
print (cars)
del cars[-1]
print (cars)
cars.remove('toyota')
print (cars)

vehicles = ['bmw', 'audi', 'hyundai', 'toyota', 'honda', 'ford', 'chevrolet', 'yugo']
for car in vehicles:
    print (car)

numList = []
for digit in range(1,5):
    numList.append(digit)
print (numList)

print (list(range(3, 21, 3))) # multiples of 3 up to 18

squares = []
for number in range(1, 8):
    squares.append(number**2)

print ('list of squares: ' + str(squares))

digits = [1, 2, 4, 5, 4, 67, 3, 2, 4, 5, 54, 6, 4, 2, 3, 4,5, 6, 4, 4]
print ('min ', min(digits)) # get the min of a number list
print ('max ', max(digits)) #get the max of a number list
print ('sum ', sum(digits)) #get the sum of a number list

doubles = [value * 2 for value in range(1, 11)]
print (doubles)



secondList = [value * 5 for value in range (1, 5)]
print(secondList)


theString = "sampleString"
print("The value of the string is: %s, along with: %s" %(theString, "Dope"))

# Now starting floating point number practice:
print("Lets get started with this: %1.3f" %(34.56632113)) #34.566

print(my_dict)
del(my_dict["key3"]) # Deleting a key from a dictionary
print(my_dict)








