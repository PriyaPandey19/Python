#conditional statment
marks = int(input("Enter the marks :"))

if(marks > 0):
    print("POSITIVE")
elif(marks == 0):
    print("ZERO")
else:
    print("NEGATIVE")     


#lists in python
food =["chole bathure", "choco waffle","mango", "apple", "gulab jamun"]
print(len(food))

print("First Value of the last:", food[0])
print("Third Value of the list:", food[3])


marks1= [99, 100, 90, 95]
print(marks1)

print(marks1[1:3])
print(max(marks1))
print(min(marks1))
marks1.append(92)
print(marks1)
marks1.sort()
print(marks1)
marks1.pop(1)
print(marks1)
marks1.remove(100)
print(marks1)
marks1.insert(1,100)

#make list
food1 = input("Enter food 1:")
food2 = input("Enter food 2:")
food3 = input("Enter food 3:")

foodList = []
foodList.append(food1)
foodList.append(food2)
foodList.append(food3)

print(foodList)
print(len(foodList))