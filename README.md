# Python Intro
- python is a programming language
## Why Python
- one of the easiest language to learn
### Python use cases
#### Python set up with Pycharm
##### Python Variables
### Types of data
- Str - string (word)
- Float - real number
- Int - Integer (decimal)
- Boolean - Yes or no (true or false)
- List 

### Github setup
- generate ssh key
- cd .ssh
- ssh-keygen -t rsa -b 4096 -C "adamhamdi85@gmail.com"
- copy public key (cat id_rsa.pub)
- add another repository on Github
- then create README.md file and connect it to the repository.

- then put in variable for each one of the following and press enter,
- git init
- git add README.md
- git commit -m "first commit"
- git status to see if its green then proceed
- git branch -M main
- git remote add origin "git@github.com:[username]/[repository].git"
- git push -u origin main

-Env Testing print("hello world")

```python

# first_name = "Adam"
# last_name = "Hamdi"
# salary = 50
# travel= 3.5
#
# print(first_name)
# print(last_name)
# print(salary)
# print(travel)
#
# print(type(last_name))
# 
# print("good morning, please enter your name ")
#
#
# print(name)
# print("hello dear ")


print("what is your first name? ")
first_name = input()
print(" what is your last name? ")
last_name = input()
print(" what is your DOB? ")
DOB = input()
print(" are you a UK resident? ")
UK_resident = input()
```

#### Git and Github
- add changes to our Git-Hub repo that we made to local host

- `git add filename` or `git add .` means push everything from current location
- `git commit -m "new markdown guide added"`
- now let's send this new data to github
- `git push -u origin main` 
- `git status`
<<<<<<< HEAD
- add `.gitignore` then `add all dependencies in this file to ensure not pushed to github`
- to pull changes from git-hub `git pull`
=======
### this change is done on github
```
These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects
```


### Intro to Data types and Operators
- `+ - * /`

###### Comparison Operators
- `>` greater than
- `<` less than
- `==` true or false
- `>=` greater than or equal
- `<=` less than or equal
```python
a = 24
b = 16
user_age = 18
print(a + b) # outcome added value of a and b
print(a - b) # outcome minus a from b
# comparison
print(a > b) # true
print(a < b) # false
print(a == b)
```
```python
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
```

```python
greeting = "Hello World!"
print(greeting)
print(greeting.isalpha()) #only letters
print(greeting.islower()) #only lowercase characters
print(greeting.startswith("H")) #stars with [argument]
print(greeting.endswith("!")) #ends with [argument]
print(greeting.isdigit()) #only numbers
```
```python
# String Slicing
# string indexing - starts from 0
# Hello World!
# 01234567891011
#            -2-1

greeting = "Hello World!"
print(greeting)
# we have a builtin method that checks the len of the string
print(len(greeting)) # length of string (or array)
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
print(Example_text.count("text"))  # counts the times [argument] appears in the string
print(Example_text.lower())  # converts string to lowercase
print(Example_text.upper()) # converts string to lowercase
print(Example_text.capitalize()) # capitalises first letter
print(Example_text.replace("with",",")) # replaces [argument1] with [argument2]

```
```python
# user data input
first_name = "adam"
last_name = "hamdi"
salary = 40

# print(first_name)
# print(last_name)
# print(first_name + " " + last_name + " " + str(salary))# because int change to str()

# F-string
print(f"Hello {first_name} {last_name}")


#
print("Good Morning, Please enter your First Name")
first_name = input()
#
print ("Enter Last Name")
last_name = input()
#
print("Enter DOB")
DOB = input()

print("Are you a Uk resident? Answer Yes or No")

uk_resident = input()


print(f'Hello   {first_name}  {last_name} {DOB} {uk_resident}')
```