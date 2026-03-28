#dictionary
student = {
    "name": "Priya Pandey",
    "city": "Jabalpur",
    "age":24,
    "rollNumber": 34
}

print(type(student))
print(student)
print(student["city"])
student["city"] = "Hong Kong"
student["favSubject"] = "Maths"
print(student)
student.pop("favSubject")
print(student)
print(student.keys())
print(student.values())

#enter the marks of 3 subjects
marks={}

marks["Maths"] = 98
marks["Chemistry"]=89
marks["Physics"]=88
print(marks)


#set
food={"paneer","sandwitch","burger","pizza"}
print(type(food))
print(food)