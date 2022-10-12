#### Dictionary
```
# What is a Dictionary - Data collection type
# Hoq to manage Dictionaries - How to manage the data using Dict
# It works as key value pair key = value
# Syntax { "name": "Sparta"      }
            #0         1
# store student's data - name, course_name, progress, completed_lessons_names
student_1 = {
    "key" : "values",
    "name": "Adam",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["lists", "tuples", "OOP"]
}
print(type(student_1))
print(student_1["stream"]) # This will explain the value saved inside stream
print(student_1["completed_lessons_names"][0])   # print list
print(student_1["completed_lessons_names"])

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])
delete an item from the list of completed_lessons_name/key
student_1["completed_lessons_names"].remove("OOP")
print(student_1["completed_lessons_names"])

# Dict Builtin Methods
# display keys only or values
# keys() values()
print(student_1.keys())

#display values only from student_1
print(student_1.values())
```