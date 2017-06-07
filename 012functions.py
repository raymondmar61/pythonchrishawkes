def my_add_function():
	print(4 + 4)

print("hello world") #in case you don't notice, print("hello world") ran first.

my_add_function()  #returns 8

def my_add_function2(first_number, second_number):
	print(first_number + second_number)
my_add_function2(5, 5)
my_add_function2("chris", " hawkes")

def my_smart_function(smartnumberone, smartnumbertwo, math_operation):
	if math_operation == "add":
		print(smartnumberone + smartnumbertwo)
	elif math_operation == "multiply":
		print(smartnumberone * smartnumbertwo)
	else:
		print("Unknown inputs")
my_smart_function(4, 5, "add")
my_smart_function(4, 5, "multiply")
my_smart_function(3, 9, "subtract")