my_string = "this is a string"
for eachcharacter in my_string:
	#print(eachcharacter)
	print(eachcharacter, end="")
print("\n")
for gcharacter in my_string:
	if gcharacter == "g":
		print("holy crap it's a g!")

fruits = ["banana","apple","pear"]
for eachfruit in fruits:
	print("I like to eat " +eachfruit+ ". ", end = "")
	if eachfruit == "banana":
		print("Priority banana print it.")
print("\n")

fruits = ["banana","apple","pear"]
for eachfruit in fruits:
	print("I like to eat " +eachfruit+ ". ", end = "")
	if eachfruit == "apple":
		print("Priority apple print it.")
		continue
print("\n")

for eachfruit in fruits:
	print("I like to eat " +eachfruit+ ". ", end = "")
	if eachfruit == "banana":
		print("Priority banana print it.")
		break
print("\n")