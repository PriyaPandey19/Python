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
food.add("kunafa")
print(food)
food.remove("sandwitch")
print(food)

languages = ["python","java","c++","python","java","c"]
print(type(languages))
programmingSet = set(languages)
print(type(programmingSet))
print(programmingSet)   
print("Divya knows these programming language", len(programmingSet))

#hw
dictionary = {
    "snobish": "nakhrebaaz",
    "propaganda": "maybe false news",
    "narcissts": "self obsessed"
}
print(dictionary)


numbers1 = {2,3,4,1}
numbers2 = {5,6,7,1}
numbers3 = numbers1.union(numbers2)
print(numbers3)
numbers4 = numbers1.intersection(numbers2)
print(numbers4)