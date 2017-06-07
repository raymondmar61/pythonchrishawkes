#Chris Hawkes 2 Strings, 3 Numbers, 4 Multi-Line Strings, 5 Lists, 6 (ARGV), 7 If Elif Else, 8 For Loops, 9 Range, 10 While Loop, 11 Comments, 12 Functions, 13 Imports, 14 Classes, 15 Sub-Classes, 16 Default Function Parameters, 17 Dictionaries, 18 kwargs, 19 Tuple, 21 Try Except

my_variable = "this is a string"
my_second_variable  = "this is some more stuff"
my_combined_variable = my_variable + " " +my_second_variable
print(my_combined_variable) #print this is a string this is some more stuff
my_variable_html = "<html><body><p>Look at this.  It's written from Python to HTML.</p></body></html>"
my_html_file = open("test.html", "w")
my_html_file.write(my_variable_html)
my_html_file.close()
print("\n")

my_number = 2
print(8 * 8) #print 64
print("Sesame street is brought to you by the letters . . . and the number " +str(my_number)+ ".  Sesame street is a production of the Children's Television Workshop.") #print Sesame street is brought to you by the letters . . . and the number 2.  Sesame street is a production of the Children's Television Workshop.
print("\n")

delimiterthreequotes = """ three quotes multi-line
okay dokey """
print(delimiterthreequotes) #print three quotes multi-line\nokay dokey
another_string = "testing"
delimiterthreequotes = """ three quotes multi-line """ +another_string+ """
okay dokey """
print(delimiterthreequotes) #print three quotes multi-line testing\nokay dokey
my_variable_html = """
	<html>
	<body>
	<p>Look at this.  It's written from Python to HTML.</p>
	</body>
	</html>
"""
animal = "cat"
print("%s ran over the hill" %animal) #print cat ran over the hill
print("%s ran over the hill" %"horse") #print horse ran over the hill
print("\n")

another_list = []
my_list = ["apple","pear","orange",1,another_list]
print(len(my_list)) #print 5
my_list = ["apple","pear","orange"]
my_list.append("banana")
print(my_list) #print ['apple', 'pear', 'orange', 'banana']
my_list.pop() #removes the last list item
print(my_list) #print ['apple', 'pear', 'orange']
my_list = ["apple","pear","orange"]
my_list.pop(0) #removes the first list item
print(my_list) #print ['pear', 'orange']
my_list = ["apple","pear","orange"]
print(my_list[0]) #print apple
my_list = ["apple","pear","orange"]
my_list.insert(1, "banana")
print(my_list) #print ['apple', 'banana', 'pear', 'orange']
my_list.remove("banana")
print(my_list) #print ['apple', 'pear', 'orange']
my_list = ["apple","pear","orange"]
my_list.extend(["banana","strawberry","tomato"])
print(my_list) #print ['apple', 'pear', 'orange', 'banana', 'strawberry', 'tomato']
my_list = ['apple', 'pear', 'orange', 'banana', 'strawberry', 'tomato']
print(my_list[0:2]) #print ['apple', 'pear']
print(my_list[-1]) #print tomato
print(my_list[::-1]) #print ['tomato', 'strawberry', 'banana', 'orange', 'pear', 'apple']
print(my_list[len(my_list)::-1]) #print ['tomato', 'strawberry', 'banana', 'orange', 'pear', 'apple']
print(my_list[-2:-4:-1]) #print ['strawberry', 'banana']
print("\n")

#comment out input to speed up running file
# my_name = input("What is your name?")
# print("hi " +my_name)
import sys
print(sys.argv[0]) #print chrishawkesallvideos.py
print("\n")

my_name = "billy"
if my_name == "chris":
	print("hi chris")
elif my_name == "billy":
	print("hey billy you suck!")
else:
	print("I don't know you!")
print("\n")

my_string = "this a string"
print(my_string[5]) #print a
for character in my_string:
	print(character) #print this a string individually each separate line
for whatever_you_want in my_string:
	if whatever_you_want == "g":
		print("holy crap it's a g!")
fruits = ["banana","apple","pear"]
for f in fruits:
	print("I like to eat " +f)
	if f == "banana":
		print("I like bananas")
for f in fruits:	
	if f == "banana":
		print("I like bananas")
		break
print("\n")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(1,6):
	print(x, end="") #print 12345
print("")
for x in range(1,6):
	print(my_list[x], end="") #print 23456
print("\n")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_number = 0
while start_number < 5:
	print(my_list[start_number])
	start_number += 1
print("\n")

"""
Anything inside these
multi-line comments here is ignored
by Python
"""

def my_add_function():
	print(4 + 4)
print("hello world") #print() is a function.  It's a built-in function.
my_add_function() #return 8
def my_add_function2(first_number, second_number):
	print(first_number + second_number)
my_add_function2(5, 6) #return 11
my_add_function2("chris", " hawkes") #return chris hawkes
def my_multiply_function(first_number, second_number):
	print(first_number * second_number)
my_multiply_function(5,2) #return 10
def my_smart_functionhere(first_number, second_number, math_operation):
	if math_operation == "add":
		print(first_number + second_number)
	elif math_operation == "multiply":
		print(first_number * second_number)
my_smart_functionhere(5,7, "add") #return 12
my_smart_functionhere(5,7, "multiply") #return 35
print("\n")

from b012functions import my_smart_function
my_smart_function(10, 123, "add") #return 133
from c012functions import *
my_smart_function(200, 223, "add") #return 423
another_function() #return holy crap this is another function
#override a function from c012functions.py.  In this case, another_function()
def another_function():
	print("I overrode this joint")
another_function() #return I overrode this joint
print("\n")

#Video 14 Classes
class Person:
	def print_name(self):
		print("chris hawkes")
chris = Person()
chris.print_name() #return chris hawkes
class Person2:
	def __init__(self, name):
		self.name = name
	def print_name(self):
		print(self.name)
raymond = Person2("raymond mar")
raymond.print_name() #return raymond mar
chrishawkes = Person2("Chris Hawkes")
chrishawkes.print_name() #return Chris Hawkes
class Person3:
	def __init__(self, name, hair_color, height):
		self.name = name
		self.hair_color = hair_color
		self.height = height
	def print_name(self, endingaftername):
		print(self.name + " " +endingaftername)	
	def print_hair_color(self):
		print(self.hair_color)	
	def print_height(self):
		print(self.height)
	def print_all(self):
		print(self.name+ " is " +str(self.height)+ " inches tall with hair color " +self.hair_color)
raymond = Person3("raymond mar", "black", 68)
raymond.print_name("by george") #return raymond mar by george
raymond.print_hair_color() #return black
raymond.print_height() #return 68
raymond.print_all() #return raymond mar is 68 inches tall with hair color black
print("\n")

#Video 15 Sub-Classes use Person 3 classe from Video 14 Classes
class Employee(Person3):
	def __init__(self, employee_id):
		self.employee_id = employee_id
	def print_employee_id(self):
		print(self.employee_id)
billy_the_employee = Employee("a123")
billy_the_employee.print_employee_id() #return a123
class Employee2(Person3):
	def __init__(self, name, hair_color, height, employee_id):
		Person3.__init__(self, name, hair_color, height)
		self.employee_id = employee_id
	def print_employee_id(self):
		print(self.employee_id)
billy_the_employee2 = Employee2("chris hawkes","brown","6-1","a123")
billy_the_employee2.print_employee_id() #return a123
billy_the_employee2.print_hair_color() #return brown
print("\n")

def optional_parameter(first_parameter = 0):
	print(first_parameter + 8)
optional_parameter(10) #return 18
optional_parameter() #return 8
print("\n")

my_dictionary_initial = {}
my_dictionary_initial["name"] = "Chris Hawkes"
print(my_dictionary_initial) #print {'name': 'Chris Hawkes'}
my_dictionary = {"name":"chris hawkes","height":"6-1"}
print(my_dictionary) #print {'height': '6-1', 'name': 'chris hawkes'}
print(my_dictionary["height"]) #print 6-1
del my_dictionary["height"]
print(my_dictionary) #print {'name': 'chris hawkes'}
my_dictionary["height"] = "6-1"
print(my_dictionary) #print {'height': '6-1', 'name': 'chris hawkes'}
for key, value in my_dictionary.items():
	print(key)
	print(value)
print("\n")

def my_keyword_argument_function(**kwargs): #keyword arguments which is a dictionary
	if kwargs["name"] == "chris hawkes":
		print("hello chris hawkes")
	if kwargs["height"] == "6-1": #kwargs can be reassigned new values
		kwargs["height"] = "6-3"
	print(kwargs)
	print(type(kwargs))
my_keyword_argument_function(name="chris hawkes", height="6-1") #return {'height': '6-3', 'name': 'chris hawkes'} \n <class 'dict'>
print("\n")

my_fruits = ("banana","pear","orange")
print(type(my_fruits)) #print <class 'tuple'>.  Tuples can't change.
for eachfruit in my_fruits:
	print(eachfruit)
my_fruits = ("banana","pear","orange","banana","pear","orange","apple")
print(set(my_fruits)) #print {'banana', 'pear', 'orange', 'apple'}
print(my_fruits) #print ('banana', 'pear', 'orange', 'banana', 'pear', 'orange', 'apple')
print(type(my_fruits)) #print <class 'tuple'>.  Tuples can't change.
setmy_fruits = set(my_fruits)
print(setmy_fruits) #print {'apple', 'orange', 'banana', 'pear'}
print(type(setmy_fruits)) #print <class 'set'>
print("\n")

while True:
	try:
		number = int(input("Enter a number? "))
	except ValueError:
		print("It's not a number!")
		break
	if number == 0:
		print("The number " + str(number))
	elif number % 4 == 0:
		print("The number " + str(number) + " is a multiple of 4 and an even number")
	elif number % 2 == 0:
		print("The number " + str(number) + " is an even number")
	else:
		print("The number " + str(number) + " is an odd number")

