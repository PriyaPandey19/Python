#expense tracker 
expenses = []
print("Welcome to Expense Tracker: Kharcha kam kiya karo")

while True:
    print("===MENU===")
    print("1.Add Expenses")
    print("2. View All Expenses")
    print("3. View Total ")
    print("4. exit")

    choice = int(input("Please Enter Your Choice: "))

    if(choice == 1):
        date= input("Whicj date: ")
        category= input("Which category(food, travel, books): ")
        description=input("In details:")
        amount= input("Enter the amount: ")


        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("\n DONE bro. Expense is added successfully..")



#2. VIEW ALL EXPENSES 
    if(choice == 2):
        if(len(expenses) == 0):
            print("No Expenses Added.")
        else:
            print("=== This is all your expense ===")
            count=1
            for eachkharcha in expenses:
                print(f"Expense Number {count} => {eachkharcha["date"]}, {eachkharcha[category]}, {eachkharcha["description"]}, {eachkharcha["amount"]}")  
                count= count+1 