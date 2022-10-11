# # let's see the operator's in action
# ### Intro to Data types and Operators
# - `+ - * /`

# ###### Comparison Operators
# - `>` greater than
# - `<` less than
# - `==` true or false
# - `>=` greater than or equal
# - `<=` less than or equal
#
# a = 24
# b = 16
# user_age = 18
# print(a + b) # outcome added value of a and b
# print(a - b) # outcome minus a from b
# # comparison
# print(a > b) # true
# print(a < b) # false
# print(a == b)

# # % operator - find the use of this operator
# # modulus operator
# #gives the remainder of the dividing left operator by right
# c = 10
# d = 100
# print(c%d)




# Boolean Builtin methods in Python - Boolean Methods
# - DRY not to repeat yourself print("")

greeting = "Hello World!"
print(greeting)
print(greeting.isalpha())
print(greeting.islower())
print(greeting.startswith("H"))
print(greeting.endswith("!"))
print(greeting.isdigit())

# String Slicing
# string indexing - starts from 0
# Hello World!
# 01234567891011
#            -2-1

greeting = "Hello World!"
print(greeting)
# we have a builtin method that checks the len of the string
print(len(greeting)) #
print(greeting[0:5])
print(greeting[6:12])
print(greeting[-12:-6])
print(greeting[-6:-1])

# String methods are available
# use var = string "asdfghhgfehgfds"
white_space = "lot's of spaces at the end             "
print(len(white_space))
# strip() removes the white spaces at the end of the strip
print(len(white_space.strip())) # this will remove all the white spaces at the end
#print(print(len(white_space)))

Example_text = " adam here's sOme text with lOt's of text"
print(Example_text.count("text"))
print(Example_text.lower())
print(Example_text.upper())
print(Example_text.capitalize())
print(Example_text.replace("with",","))




