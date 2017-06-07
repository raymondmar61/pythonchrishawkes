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