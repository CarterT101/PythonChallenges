import datetime
import json
import math
import random
import re
import os
from abc import ABC, abstractmethod

# creating variable
x = 5
print(x)

# remember, python is dynamic, so you can declare type of variable, this is called 'casting'

string = str("Hello")
integer = int(3)

print(string)
print(integer)

print('Hello')  # can use "" or ''

x = float(2.8)  # also works as just x=2.8

print(x)

print(type(x))  # prints data type of variable

a = 50      # 110010  the '&' symbol goes through the binary version. if both have a 1, the outputted binary is a 1
b = 25      # 011001
c = a & b   # 010000
print(c)

x, y, z = "Orange", "Banana", "Cherry"  # assigning multiple values on one line
print("\nAssigning multiple values in one line")
print(x, y, z)

x = y = z = "Orange"  # assigning one value to multiple variables
print("\nAssigning one value to multiple variables")
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]  # extracting values into variables
x, y, z = fruits
print("\nUnpacking collection")
print(x)
print(y)
print(z)


def myfunc():
    global x  # creating global variable
    x = "fantastic"


myfunc()

print("Python is " + x)

x = random.randrange(1, 10)  # making random range
print("\nHello " + str(x))

y = "Hello"[0]  # prints first letter of string
print(y)

b = "Hello, World!"  # gets characters from position 2 to 5, which is 'llo'
print(b[2:5])

a = "Hello, World!"  # split() method splits string into substring if it finds instances of the separator
print(a.split(","))  # returns ['Hello', ' World!']

# strings are arrays, so we can loop through them

for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)  # gives bool data back, checks if 'free' is in the variable 'txt'

txt = "The best things in life are free!"
if "free" in txt:  # checks if 'free' is in variable 'txt' using 'if' statement
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("\nexpensive" not in txt, ", expensive is not in variable txt")  # checks if expensive is NOT in variable txt

print("\nhi world".upper())  # makes them all capitalized #.upper is a built-in function

print("\nHello".replace("H", "Y"))  # replaces h with y

age = 36
txt = "My name is John, and I am {}"  # formatting
print(txt.format(age))

txt = "hello, and welcome to my world."

x = txt.capitalize()  # how to use string methods

print(x)

txt = "For only {price:.2f} dollars!"  # puts two decimal spots
print(txt.format(price=49))  # output is [For Only 49.00 dollars!]

list1 = ["Hello", "World"]  # a list

print(type(list1))  # gets type of list

mytuple = ("apple", 1, True)  # tuple, ordered and unchangeable, can have contain different data types

myset = {"apple", "banana", "cherry"}  # set, unordered, unchangeable, not indexed, can add and remove items,
# no duplicate, can contain different data types

thisdict = {  # dictionary, ordered, changeable, does not allow duplicates
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist.pop(1)  # 'del thislist[1]' does the same thing, del can also delete the whole list 'del thislist'
print("I used .pop method to get rid of index 1: ", thislist)
thislist.clear()
print("I have cleared the list: ", thislist)

# my-var is NOT a legal variable name

z = "   This is      "

z2 = z.strip()  # .strip gets rid of whitespace in front and behind

print(z2 + " sentence")

"""
this is how to write a comment in more than one line

"""


class Car:
    def __init__(self, speed, color):  # when you provide parameters, now you need to provide arguments
        # serves as constructor for class (NOT ACTUALLY A CONSTRUCTOR, ONLY BEHAVES AS ONE), used to
        # initialize some attributes or functions, first method which will be called when you create instance of class
        print('\n__init__ is called')

        self.speed = speed  # self is current object, assigning attribute to argument, in this case, .speed to speed
        self.color = color  # this allows you to call a specific attribute
        print(speed)
        print(color)


ford = Car(200, 'blue')  # creating instance of class,
# honda = Car() this alone would cause an error because they do not give the arguments needed by __init__
audio = Car(150, 'red')

# ford.speed = 200  # initializing the value of speed

print(ford.speed)  # without the self.speed, this would not work.


def myTest(*args):  # can pass in undefined number of arguments, written in tuple form
    for arg in args:
        print(arg)


myTest('This is a test', 'ok', 2)


def myTest1(**kwargs):  # pass in undefined arguments, represents key-value pair
    print("kwargs", kwargs)


myTest1()
myTest1(first="1")
myTest1(second="2", third="3")


class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
        # telling us to pass in an argument, but won't tell you what kind of data it will be

    @abstractmethod
    def payment(self, amount):
        pass


class DebitCardPayment(car):  # defined how to implement payment function from parent paySlip class
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit'.format(amount))


obj = DebitCardPayment()
obj.paySlip(400)
obj.payment("$400")

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

thislist = ["apple", "banana", "cherry"]  # loop through list, for loop
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]  # loop through index numbers
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]  # loop using while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:  # adding fruit to new list if it starts with 'a'
    if "a" in x:
        newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print("This is the list comprehension list: ", newlist)

#  newlist = [expression for item in iterable if condition == True]
#  condition is like a filter that only accepts item that valuate to true
# iterable can be any iterable object, like list, tuple, set, etc
# you can use the range() function to create iterable

newlist = [x if x != "banana" else "orange" for x in fruits]
# return the item if it is not banana, if it is banana return orange
newlist.sort(reverse=True)  # sorts list alphabetically, descending. Leave () blank for ascending
print(newlist)

newlist = [x for x in range(10) if x < 5]
print("Number list of numbers lower than 5: ", newlist)


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)  # sorts the list based on how close the number is to 50
thislist.reverse()  # reverses list
print(thislist)

# convert tuple into list
x = ("apple", "banana", "cherry")  # tuple
y = list(x)  # now a list
y[1] = "kiwi"  # changing item in tuple, now list
x = tuple(y)  # changing back to tuple. DO THIS SAME PROCESS TO ADD NEW ITEMS SINCE TUPLES ARE UNCHANGEABLE, IMMUTABLE

print(x)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits  # the asterisk will add the remaining values to that variable

print(green)
print(yellow)
print(red)

x = fruits * 2  # multiplies tuple to create duplicates
print(x)
y = x.count("apple")  # counts how many times "apple" is in the tuple
print("apple appears " + str(y) + " times")

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")  # add item to set

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)  # add set to set

thisset.remove("banana")  # removes specified item

print(thisset)

thiscar = {  # values in dictionary items can be of any data type, string, int, bool, list
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print(thisdict.keys())
print(thisdict.values())

thiscar["year"] = 2020
print(thiscar["year"])

print(thiscar.items())  # return each item in a dictionary as tuples in a list

for x in thiscar.values():  # prints values
    print(x)

for x, y in thiscar.items():  # prints keys and values
    print(x, y)

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

for x, y in myfamily.items():
    print(x, y)

a = 200
b = 33
if a > b: print("a is greater than b")  # shorthand if statement
print("A") if a > b else print("B")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # ends while loop
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # returns control to the beginning of the while loop, in this case it would skip printing 3
    print(i)
else:
    print("i is no longer less than 6")  # runs once while loop is over

for x in "string":
    print(x)

for x in fruits:
    print(x)
    if x == "strawberry":
        break

for x in range(2, 6):  # stops before 6, so ends at 5
    print(x)

for x in range(2, 30, 3):  # 2 through 30 with 3 increment
    if x == 23: break  # else statement wont execute if break statement is here
    print(x)
else:
    print("Finished")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


def my_function():
    print("Hello from a function")


my_function()  # calls function


def myName(fname):  # giving parameters
    print(fname + " Thurman")


myName("Carter")  # calling function and giving arguments


def myKids(*kids):  # * is if the number of arguments is UNKNOWN
    print("The youngest child is " + kids[-1])  # prints the last item in given arguments


myKids("Carter", "Brandon", "Kennyah", "Evan")


def myList(**kid):  # if the number of keyword arguments is UNKNOWN
    print("The oldest child is " + kid["child3"])


myList(child3="Brandon", child2="Evan", child1="Kennyah")


def myCountry(country="United States"):  # default value
    print("I am from " + country)


myCountry()
myCountry("Sweden")


def myFood(food):
    for x in food:
        print(x)


myFood(fruits)  # passing in list, can be a string, set, tuple, etc


def myReturn(x):
    return 5 * x  # returns value


print(myReturn(3))

# lambda arguments : expression

x = lambda a, b: a + b + 10
print("This is lambda: " + str(x(5, 5)))  # can take multiple arguments


# this function will always double the number you send in
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(13))
print(mytripler(3))

# array, use a list to make an array. arrays are a single data type, faster than a list
shops = ["Amys", "Chick", "McDonald"]

shops[0] = "Redbird"

print(shops[0])


class MyClass:  # create a class named MyClass with a property named x
    x = 5
    variable = "Yes"


p1 = MyClass()  # creating an object
print("This is a property of MyClass: " + str(p1.x) + " " + p1.variable)


class Person:  # parent class
    def __init__(self, name, age):
        self.name = name  # properties
        self.age = age

    def mygreet(self):  # function inside class
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old.")


p2 = Person("John", 36)  # creating object

print(p2.name + " " + str(p2.age))  # using object to get properties
p2.age = 43  # modifying age property
p2.mygreet()  # calling function inside class


class Student(Person):
    pass  # pass so we do not need to add any other properties or methods to the class


p3 = Student("Evan", 20)  # creating child object
p3.mygreet()  # using function from parent class with child class object


class Employee(Person):
    def __init__(self, fname, age, year):
        super().__init__(fname, age)  # super() funct will make child class inherit all methods and props from parent
        self.hiringyear = year  # creating new property

    def welcome(self):
        print("Welcome", self.name, "to the class of", self.hiringyear)  # new function


p4 = Employee("Carter", 21, 2022)  # creating new object

print(p4.name + " " + str(p4.age) + " " + str(p4.hiringyear))

p4.welcome()  # calling new function

myit = iter(fruits)  # lists, tuples, etc are iterable containers. can do this with basic for loop

print(next(myit))
print(next(myit))
print(next(myit))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:  # stops at 20
            x = self.a
            self.a += 1  # goes up by 1 each iteration
            return x
        else:
            raise StopIteration


myclass = MyNumbers()  # creating object
myiter = iter(myclass)  # making an iterator

for x in myiter:  # iterating through iteration, above the function will stop it so it is not infinite
    print(x)

x = datetime.datetime.now()  # making datetime object
print(x)
print(x.year)
print(x.strftime("%A"))  # prints weekday. strftime() method for formatting date objects into readable strings

x = datetime.datetime(2020,5,17)  # using datetime() class (constructor) of datetime module, this class requires 3 para

print("This is the date: " + str(x))

x = pow(4,3)  # 4 to the power of 3
print(x)

x = math.sqrt(64)
print(x)

# json code
x = '{ "name":"John", "age":30, "city":"New York" }'
# parsing x
y = json.loads(x)
# result is a python dictionary
print(y["age"])

# python object
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# convert into JSON
y = json.dumps(x)
# json string is the result
print(y)

# RegEx practice
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # search string if it starts with 'The' and ends with 'Spain'

txt = "The rain in Spain"  # 'x' is the Match object, has properties and methods used to retrieve info
x = re.split("\s", txt)  # returns a list where string has been split up at each white-space character
print(x)  # output is ["The", "rain", "in", "Spain"]

try:
    print(we)
except NameError:                           # prints if try doesn't work
    print("Variable we is not defined")
except:
    print("An exception occured")
finally:                                    # goes regardless of error or not
    print("The 'try except' is finished")

# example code of where finally: would be useful, always close the source
"""
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
"""

# user input
"""
username = input("Enter username:")
print("Username is: " + username)
"""


# file handling

# open() function takes two parameters; filename and mode
# r = read
# a = append
# w = write
# x = create

f = open("C:\\Users\hoove\Documents\School\Python Practice\demofile.txt", "r")
print(f.read(5))  # number represents amount of characters we want to return, leave blank for whole file
f.close()

f = open("C:\\Users\hoove\Documents\School\Python Practice\demofile.txt", "w")
f.write("Now the file has this line")
f.close()

f = open("C:\\Users\hoove\Documents\School\Python Practice\demofile.txt", "r")
print(f.read())
f.close()

f = open("C:\\Users\hoove\Documents\School\Python Practice\demofile.txt", "a")
f.write("\nNow the file has another line")
f.close()

f = open("C:\\Users\hoove\Documents\School\Python Practice\demofile.txt", "r")
print(f.read())
f.close()

f = open("mytestfile.txt", "x")
f.close()

if os.path.exists("mytestfile.txt"):
    os.remove("mytestfile.txt")
else:
    print("File does not exist")

