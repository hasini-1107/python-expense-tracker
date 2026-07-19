expenses = []
next_id = 1
choice = "y"
while choice == "y":
    option = int(
        input("choose: 1.add your expenses/ 2. view all expenses/ 3. total spending/ 4. category filter/ 5. delete an expense "))
    if option == 1:
        print("ADD YOUR EXPENSE")
        Amount = int(input("Amount: "))
        Category = input("Category: ").lower()
        Description = input("Description: ")
        expense = {
            "ID": next_id,
            "Amount": Amount,
            "Category": Category,
            "Description": Description
        }
        expenses.append(expense)
        next_id = 1 + next_id

    elif option == 2:
        print("all expenses:")
        for expense in expenses:
            print("id: ", expense["ID"],
                  "\namount: ", expense["Amount"],
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
        found = False
        for expense in expenses:
            if category == expense["Category"]:
                found = True
                print("id: ", expense["ID"],
                      "\namount: ", expense["Amount"],
                      "\ncategory: ", expense["Category"],
                      "\ndescription: ", expense["Description"])
        if not found:
            print("no expense in this category")

    elif option == 5:
        id = int(input("print the ID to delete the expense: "))
        found = False
        for expense in expenses:
            if id == expense["ID"]:
                found = True
                expenses.remove(expense)
                break
        if not found:
            print("invalid id")

    choice = input("do you wanna add another expese:(y/n) ").lower()
