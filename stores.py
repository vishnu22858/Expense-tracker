from utils import load_json, save_json
import random
from datetime import datetime

class UserStore:
    """ 
    expected user format:
        {
            "user_id" : 
            "username": "name"
            "password": 
            "created at": 
    
        }
    """

    def __init__(self, path):
        self.path = path
        self.data = load_json(self.path, default = {"users": []})

    def save(self):
        save_json(self.path, self.data)

    def add_user(self, user):
        self.data["users"].append(user)
        self.save()

    def find_user_by_username(self, username):
        for user in self.data["users"]:
            if user["username"] == username:
                return user

        return None


class ExpenseStore:
    """
    expected expense format:
        {
            "expense_id":
            "logged_in_user_id":
            "amount":
            "category": 
            "description":
            "created_at":
        }
    """


    def __init__(self, path):
        self.path = path
        self.data = load_json(self.path, default = {"expenses": []})

    def save(self):
        save_json(self.path, self.data)

    def add_expense(self, logged_in_user_id):
        amount = int(input("\nEnter the amount: "))
        category = input("Enter the category: ")
        description = input("Enter short description: ")

        expense = {
                "expense_id": str(random.random()), 
                "logged_in_user_id": logged_in_user_id,
                "amount": amount,
                "category": category,
                "description": description,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.data['expenses'].append(expense)
        self.save()
        print("Expense added!")


    def view_total_expense(self, user_id):
        
        total_expense = 0
        total_expense_list = []

        for expense in self.data['expenses']:
            if expense["logged_in_user_id"] == user_id:
                total_expense_list.append(expense)

        for expense in total_expense_list:
            print("\n")
            print("Category: ", expense["category"])
            print("Amount: ", expense["amount"])
            print("Description: ", expense["description"])


        for expense in total_expense_list:
            total_expense += expense["amount"]

        print("\nTotal expenses = ", total_expense)


    def view_expense_by_category(self, user_id):
        """Loop through the expenses and append the expenses of the particular user by matching id to a 
        new list.
        Loop through new list and create a dictionary of categories.
        """
        
        expense_list = []
        categories = {}

        for expense in self.data['expenses']:
            if expense["logged_in_user_id"] == user_id:
                expense_list.append(expense)

        for expense in expense_list:
            category = expense["category"]
            amount = expense["amount"]

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

       
        print("\nCategories with the amount spent: ")
        print(categories)
        


 