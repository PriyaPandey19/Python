def sumFunc():
    a=4
    b=8
    sum=a+b
    print(sum)


sumFunc()    

#welcome message
def welcome_message():
    print("Welcome to Python Programming")

welcome_message()   


#quote
def inspire():
    print("Success doesn’t come from what you do occasionally, it comes from what you do consistently. Priya")

inspire()


#food morning 
def good_morning():
    print("Good Moening, Saumya!")

good_morning()
good_morning()






#function with params and argument
def average(a,b):
    averageValue= (a+b)/2
    print(averageValue)

average(5, 10)
average(7, 10)
average(80, 98)    


#show anme and age
def show_age(name="Saumya Singh", age=25):
    print(f"{name} is {age} years old")

show_age("Priya Pandey",21)    


#fav food
def fav_food(food):
    print(f"Saumya loves {food}")

fav_food("pizza")


#return function
def multipy(a=10, b=10):
    return a*b

result = multipy()
print(result)

#sqrt num
def square(num=10):
    return num**2

print(square(3))



#count consonent and vowel
def func(userInput):
    vowels ="aeiouAEIOU"

    countVowel = 0
    countConsonent = 0

    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel = countVowel +1
            else:
                countConsonent = countConsonent +1    

    return countConsonent, countVowel   

#function Call
consonent, vowel = func("Priya Pandey")
print(consonent, vowel)         