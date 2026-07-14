expenses = []
choice = "y"
while choice == "y":
    option = int(
        input("choose 1.add your expenses/ 2. view all expenses/ 3. total spending/ 4. category filter: "))
    if option == 1:
        print("ADD YOUR EXPENSE")
        Amount = int(input("Amount: "))
        Category = input("Category: ").lower()
        Description = input("Description: ")
        expense = {
            "Amount": Amount,
            "Category": Category,
            "Description": Description
        }
        expenses.append(expense)

    elif option == 2:
        print("all expenses:")
        for expense in expenses:
            print("amount: ", expense["Amount"],
                  "\ncategory: ", expense["Category"],
                  "\ndescription: ", expense["Description"])

    elif option == 3:
        print("total amount spend: ")
        amount = 0
        for expense in expenses:
            amount = amount + expense["Amount"]
        print(amount)

    elif option == 4:
        category = input("enter category to filter: ").lower()
        for expense in expenses:
            if category == expense["Category"]:
                found = True
                print("amount: ", expense["Amount"],
                      "\ncategory: ", expense["Category"],
                      "\ndescription: ", expense["Description"])
        if not found:
            print("no expense in this category")

    choice = input("do you wanna add another expese:(y/n) ").lower()
