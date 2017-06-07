#kwargs stands for keyword arguments.  I accept an unlimited amount of keyword arguments inside the function.  Returns like a dictionary
def my_keywords_argument_function(**kwargs):
	print(kwargs)
	print(type(kwargs))
my_keywords_argument_function(name="chris hawkes", height="6-1") #returns {'name': 'chris hawkes', 'height': '6-1'} /n <class 'dict'>

def my_keywords_argument_function2(**kwargs):
	if kwargs["name"] == "chris hawkes":
		kwargs["name"] = "billy bob"
	print(kwargs)
my_keywords_argument_function2(name="chris hawkes", height="6-1") #returns {'name': 'billy bob', 'height': '6-1'}
