from auth import signup, login
from stores import UserStore, ExpenseStore

def show_start_options():
    "Prints the start options"
    print("\nWelcome to Expense tracker")
    print("1. Signup ")
    print("2. Login")
    print("3. Exit\n")

def show_login_options():
    """Shows the options after logging in"""
    
    print("\nLogged in options:")
    print("1. Add Expense with amount, category and a short description")
    print("2. View total expenses")
    print("3. View expenses grouped by category")
    print("4. Logout\n")


def main():
    "Main function to run the app"

    users = UserStore("data/users.json")
    expenses = ExpenseStore("data/expenses.json")

    while True:
        show_start_options()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            signup(users = users)

        elif choice == '2':
            user = login(users = users)
            if not user:
                return "Login Failed"

            print(f"Welcome {user["username"]}, You have successfully logged in!")
            
            while True:
                show_login_options()
                ch = input("Enter your choice:")

                if ch == '1':
                    expenses.add_expense(logged_in_user_id= user["user_id"])

                elif ch == '2':
                    expenses.view_total_expense(user_id= user['user_id'])

                elif ch == '3':
                    expenses.view_expense_by_category(user_id= user['user_id'])

                elif ch == '4':
                    print("Logging out....")
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Exiting....")
            return

        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()