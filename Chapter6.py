#while loops

num = 1

while num<=10:
    print(num)
    num += 1

print("Now we are out of moves...")  

#to cprint the even number
i = 1
while(i<=50):
    if(i%2 == 0):
        print(i)
    i+=1    


#to find the sum of natural number
n = int(input("Enter the natural number."))
sum = 0

while n>=1:
    sum = sum+n
    n=n-1

print("Sum=", sum)
print("n= ",n)    



#print star pattern

n =1
while n<=4:
    print("*" * n)
    n+=1


#print number inforont of name
k = 1
while k<=5:
    print(k, "Priya Pandey")
    k+=1

#print multiplication table
i=1
num = int(input("Enter the number:"))
while i<=10:
    print(f"{num} X {i} = {num*i}")
    i+=1    


#for loop
foodList=["cake","mango","pizza"]
for item in foodList:
    print(item)


collegeList =("NIT-Delhi","Global","IIT-D")
for eachItem in collegeList:
    print(eachItem)    



#for with range
for item in range(1, 8, 1):
    print(item)
    


for number in range(2, 20, 2):
    print(number)
    print("This is done")


p=1
while(p<=50):
    if(p%5 == 0):
        print("Priya Pandey")
    else:
        print(p)
    p+=1    
           

#square root
for item in range(1, 10, 1):
    print()
           