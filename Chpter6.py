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
