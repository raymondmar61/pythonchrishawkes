my_variable = "this is a string"
my_second_variable = "this is some more stuff"
my_combined_variable = my_variable + " " + my_second_variable
print(my_combined_variable)

my_variable_html = "<html><body><p>Look at this.  It's written from Python to HTML.</p></body></html>"
my_html_file = open("test.html", "w")
my_html_file.write(my_variable_html)
my_html_file.close()

i = 1
my_html_file = open("test2.html","a")
while i <= 10:
 	my_variable_html = "<p>The number is "+str(i)+".</p>\n"
 	my_html_file.write(my_variable_html) #must be string to write
 	i += 1
writemustbevariable = ("<p>my_html_file = open() command before while loop.</p>")
my_html_file.write(writemustbevariable)
my_html_file.close()