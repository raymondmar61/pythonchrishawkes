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
#chris.print_name() #returns CHRIS HAWKES, because there is another_value parameter, I must comment chris.print_name()
chris.print_hair_color() #returns brown
chris.print_height() #returns 6-1
chris.print_name(" this is some more crap") #returns CHRIS HAWKES this is some more crap

#subclass of Person3
class Employee(Person3):
	def __init__(self, employee_id):
		self.employee_id = employee_id
	def print_employee_id(self):
		print(self.employee_id)
chris = Person3("CHRIS HAWKES","brown","6-1")
billy_the_employee = Employee("a123")	
billy_the_employee.print_employee_id() #returns a123
# billy_the_employee.print_hair_color() #returns error message AttributeError: 'Employee' object has no attribute 'hair_color', because of error I must comment out

#subclass of Person3 complete
class Employee2(Person3):
	def __init__(self, name, hair_color, height, employee_id):
		Person3.__init__(self, name, hair_color, height)
		self.employee_id = employee_id
	def print_employee_id(self):
		print(self.employee_id)
billy_the_employee = Employee2("billy","black","5-1","a1232")
billy_the_employee.print_employee_id() #returns a1232
billy_the_employee.print_hair_color() #returns black
billy_the_employee.print_height() #returns 5-1
billy_the_employee.print_name(" additional more crap") #billy additional more crap