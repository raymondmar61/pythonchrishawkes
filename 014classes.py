class Person:
	def print_name(self):
		print("chris hawkes")
chris = Person()
chris.print_name() #returns chris hawkes

#don't write Person2 Class
class Person2:
	def assign_name(self):
		self.name = "Chris Hawkes"
	def print_name(self):
		print(self.name)
chris = Person2()
chris.assign_name()
chris.print_name() #returns Chris Hawkes

#instead, write Person2b Class
class Person2b:
	def __init__(self, name):
		self.name = name
	def print_name(self):
		print(self.name)
chris = Person2b("CHRIS HAWKES")
chris.print_name() #returns CHRIS HAWKES

class Person3:
	def __init__(self, name, hair_color, height):
		self.name = name
		self.hair_color = hair_color
		self.height = height		
	def print_name(self, another_value):
		print(self.name + another_value)
	def print_hair_color(self):
		print(self.hair_color)
	def print_height(self):
		print(self.height)
chris = Person3("CHRIS HAWKES","brown","6-1")
#chris.print_name() #returns CHRIS HAWKES, because there is another_value variable, I must comment chris.print_name()
chris.print_hair_color() #returns brown
chris.print_height() #returns 6-1
chris.print_name(" this is some more crap") #returns CHRIS HAWKES this is some more crap
