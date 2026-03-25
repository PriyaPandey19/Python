str1 = "Hello"

print(len(str1))

#print ur name and length

str2 = input("Enter your name :")
print(str2[0])
print(str2[len(str2) - 1])
print(len(str2))

#slicing
str3 = "GulabJamun"
firstHalf = str3[0:5]
trialFirstHalf = str3[:5]
trialSecondHalf = str3[0:]

print(firstHalf)
print(trialFirstHalf)
print(trialSecondHalf)


#favourite food
str4 = input("Enter your food item :")  #maggie
mid = len(str4)//2
middleThree = str4[mid-1:mid+2]
lastThree = str4[3:]
print(middleThree)
print(lastThree)


#methods
str5 = "Priya pandey"
print(str5.upper())
print(str5.lower())
print(str5.title())
print(str5.find("ya"))
print(str5.replace("pandey", "#"))
print(str5.count("a"))


str6 = input("Enter the sentence :")
lowercase = str6.lower()
replaceUnderscore = str6.replace(" ", "_")
print(lowercase)
print(replaceUnderscore)


#emoji coverter
msg = input("Enter your message :")
msg = msg.replace(":)", "😀")
msg = msg.replace(":(","🙁")
msg = msg.replace(":D","😆")
msg = msg.replace(";)","😉")
print(msg)                  
