another_list = []
my_list = ["apple","pear","orange",1, another_list]
print(my_list)
print(len(my_list))
my_list = ["apple","pear","orange"]
my_list.append("banana")
print(my_list) #returns ['apple', 'pear', 'orange', 'banana']
print(len(my_list))
my_list.pop() #removes last entry in my_list.  Last In First Out.
print(my_list) #returns ['apple', 'pear', 'orange']

my_list = ["apple","pear","orange","banana"]
#my_list.pop(0) #removes first entry in my_list.  First In First Out.
fifo = my_list.pop(0) #save my_list.pop(0) in variable fifo
print(my_list) #returns ['pear', 'orange', 'banana']
print(fifo) #returns apple

my_list = ["apple","pear","orange","banana"]
print(my_list[3]) #returns banana
my_list.insert(1, "grape")
print(my_list) #returns ['apple', 'grape', 'pear', 'orange', 'banana']
my_list.remove("grape")
print(my_list) #returns ['apple', 'pear', 'orange', 'banana']
my_list.extend(["grape","strawberry","cherry"])
print(my_list) #returns ['apple', 'pear', 'orange', 'banana', 'grape', 'strawberry', 'cherry']

my_list = ["apple","pear","orange","banana"]
new_list = my_list[0:2]
print(new_list) #returns ["apple","pear"]

slicing = ['apple', 'pear', 'orange', 'banana', 'grape', 'strawberry', 'cherry']
new_list = slicing[1:4]
print(new_list) #returns ["pear", "orange","banana"]

slicing = ['apple', 'pear', 'orange', 'banana', 'grape', 'strawberry', 'cherry']
new_list = slicing[-1]
print(new_list) #returns cherry

slicing = ['apple', 'pear', 'orange', 'banana', 'grape', 'strawberry', 'cherry']
new_list = slicing[3:]
print(new_list) #returns ['banana', 'grape', 'strawberry', 'cherry']