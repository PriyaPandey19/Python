food = "Samosa"
age=25
area=670.98
name="khushi"

print(type(name))
print(type(age))

#implict conversion
x=5
y=7
z=x+y

print("answer is", z)


#explicit conversion
num = input("Enter the value:")
convertedValue = float(num)
print("Original Value", num, "Data Type", type(num))
print("Converted Value", convertedValue, "Data Type", type(convertedValue))

#logical opeartor
print(x==y or x<y)
print(not(x<y))


#take input in celsius and print f and kelvin
num = input("Enter the value in celsius :")
convertedValue = int(num)
faherenheit = (convertedValue * 9/5) + 32
print("Faherenheit value:",faherenheit)
convertedValue1 = float(num)
kelvin = convertedValue1  + 273.15
print("Kelvin value:",kelvin)



#Bill split calculator
billAmount = int(input("Enter the bill amount :"))
frnds = int(input("Enter the total no. of frnds :"))

splitAmount = billAmount/frnds
print("Eack will pay:", splitAmount)

