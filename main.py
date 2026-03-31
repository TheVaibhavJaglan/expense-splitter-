from expense_manager import add_expense, show_balances

def menu():
    while True:
        print("\n1. Add Expense")
        print("2. Show Balances")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Who paid? ")
            amount = float(input("Amount: "))
            participants = input("Participants (comma separated): ").split(',')

            add_expense(name, amount, participants)

        elif choice == '2':
            show_balances()

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice")

menu()
