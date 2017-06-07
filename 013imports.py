#import one function from a file
from b012functions import my_smart_function
my_smart_function(5,5,"add")

#import all functions from a file
from c012functions import *
my_smart_function(10,10,"multiply")
another_function()

#override a function from c012functions.py.  In this case, another_function()
def another_function():
	print("I overrode this joint")
another_function()