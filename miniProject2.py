import datetime
import time

name = input("Welcome, Enter your name...")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("GOOD MORNING", name)
elif 11 <= presentHour <= 17:
    print("GOOD AFTERNOON", name)
elif 17 <= presentHour <= 20:
    print("GOOD EVENING", name)
else:
    print("GOOD NIGHT", name)            


print("Namste! Welcome to ChatBot")
print("You can ask me basic question! Type 'bye' to exit from the bot")


responses ={
    "hello": "Hi, Welcome . How are you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep Going! Never Give Up..",
    "happy": "Great to hear that",
    "functions kya hote hai": "jakar chapter 7 dekho"
    
}

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I will learn it soon...." 

while True:
    userInput = input("Please ask your question:")
    reply = getResponseOfBot(userInput)
    print("Bot response :", reply)

    if "bye" in userInput.lower():
        break