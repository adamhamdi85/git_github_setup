# Data Collections
# Lists
# Tuples
# Dict

# Lists
# syntax ["sdfghgf" , "fghjkl" , "wertgyhjk,"]

# apply DRY
shopping_list = ["ketchup", "fanta", "eggs", "bread"]
print(shopping_list)
print(type(shopping_list))
(shopping_list.append("chicken")) #add an item to the list
print(shopping_list)
print(shopping_list[2])
shopping_list[2] = "ice cream"
print(shopping_list)
# find out how to remove an item from the list
shopping_list.pop()
shopping_list.remove("fanta")
print(shopping_list)



# Can list have multiple data types
multiple_type = [1 ,2 ,3, "one", "five", "ten"]
print(multiple_type)
print(multiple_type[2])

# Tuples
# Immutable - cant be changed - edited - added
# user_details = DOB - country name - city name
# syntax ("")
essentials = ("milk", "paracetamol", "drinks")
print(essentials)
print(type(essentials))
# what is the difference between lists and tuples
# tuples cant change variables
# essentials [0] = "coffee"
print(essentials)