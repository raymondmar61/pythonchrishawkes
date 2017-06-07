#tuple uses (), list uses [], dictionary uses {}, set is {}
my_fruit = ("banana","pear","orange","banana","pear","orange","apple")
for eachfruit in my_fruit:
	print(eachfruit)
print(type(my_fruit)) #returns <class 'tuple'>
my_fruit = set(my_fruit)
for eachfruit in my_fruit:
	print(eachfruit)

listmy_fruit = ["banana","pear","orange","banana","pear","orange","apple"]
print(listmy_fruit) #returns ['banana', 'pear', 'orange', 'banana', 'pear', 'orange', 'apple']
listmy_fruit = set(listmy_fruit)
print(listmy_fruit) #returns {'orange', 'banana', 'apple', 'pear'}
print(type(listmy_fruit)) #returns <class 'set'>