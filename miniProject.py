#expense tracker 
expensesList = []
print("Welcome to Expense Tracker: Kharcha kam kiya karo")

while True:
    print("===MENU===")
    print("1.Add Expenses")
    print("2. View All Expenses")
    print("3. View Total ")
    print("4. exit")

    choice = int(input("Please Enter Your Choice: "))

    if(choice == 1):
        date= input("Which date: ")
        category= input("Which category(food, travel, books): ")
        description=input("In details:")
        amount_input = input("Enter the amount: ")
        try:
            amount = float(amount_input)
        except ValueError:
            print("Invalid amount entered. Please enter a number.")
            continue

        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n DONE bro. Expense is added successfully..")



#2. VIEW ALL EXPENSES 
    elif(choice == 2):
        if(len(expensesList) == 0):
            print("No Expenses Added.")
        else:
            print("=== This is all your expense ===")
            count=1
            for eachkharcha in expensesList:
                print(f"Expense Number {count} => {eachkharcha["date"]}, {eachkharcha["category"]}, {eachkharcha["description"]}, {eachkharcha["amount"]}")  
                count= count+1 

#3. View All Spending
    elif(choice == 3):
        total=0
        for eachkarcha in expensesList:
            total = total + eachkarcha["amount"]

        print("\n TOTAL KHARCHA =", total)


#4 EXIT
    elif(choice == 4):
        print("Thank You")
        break

    else:
        print("Invalid Choice. TRY AGAIN")



                