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

    def __init__(self):
        print("Whenever a new object is created I am called automatically")

student1 = Student();
student2 = Student();        

