#my_dictionary["name"] = "Chris Hawkes"
#print(my_dictionary["name"]) #returns Chris Hawkes

my_dictionary = {"name":"Chris Hawkes","height": "6-1"}
print(my_dictionary["height"])
del my_dictionary["height"]
print(my_dictionary)
my_dictionary["height"] = "6-1"
print(my_dictionary)
for key, value in my_dictionary.items():
	print(key)
	print(value)

for key in my_dictionary:
	print(my_dictionary[key]) #returns 6-1 \n Chris Hawkes