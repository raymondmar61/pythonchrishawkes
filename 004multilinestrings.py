my_multiline_variable = '''
this is a test
line 2
okay okay
line three
line four
line cinqo
'''
print(my_multiline_variable) #returns mul_multinline_variable all lines own separated line just like the defined text

anotherstring = "testing"
my_variable_html = '''
<html>
<body>
<p>Look at this.  It's written from Python to HTML.</p>
<p>this is a test</p>
<p>line 2</p>
'''+ anotherstring + '''
<p>line three</p>
<p>line four</p>
<p>line cinqo</p>
</body>
</html>
'''
my_html_file = open("test004.html", "w")
my_html_file.write(my_variable_html)
my_html_file.close()

animal = "cat"
print("%s ran over the hill" %animal)