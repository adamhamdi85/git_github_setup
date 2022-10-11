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
### this change is done on github
