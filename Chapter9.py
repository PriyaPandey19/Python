#class creation
class Vehicle:
    milege="10"
    color="black"

car = Vehicle()
print(car.color)
bike = Vehicle()
print(bike.milege)  


#create 2 object with diffrent vaLUEs

class Laptop:
    brand="default"
    RAM="default 3GB"
    price= "default"

Laptop1 = Laptop()
Laptop1.brand="Macbook"

Laptop2 = Laptop()
Laptop2.brand="Dell"

print("Laptop 1 :", Laptop1.brand)
print("Laptop 2 :", Laptop2.brand)

#init constructor
class Student:
    schoolName ="ABE School"

    def __init__(self,name, course):
        self.name = name
        self.course = course

student1 = Student("khushi", "BTech")
print("Studen1 Name-", student1.name)
student2 = Student("Ankit", "BCom")
print("Studen2 Name-", student2.name)

#average of marks
class People:
    def __init__(self,name, listOfMarks):
        self.name = name
        self.listOfMarks = listOfMarks

    def average(self):
        sum=0
        for eachValue in self.listOfMarks:
            sum = sum+eachValue

        average = sum /3
        print("Average is:", average)

student1 = People("Aditya",[80,89,89])
student1.average()



