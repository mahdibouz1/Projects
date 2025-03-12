# coding=utf-8
import sqlite3

connect = sqlite3.connect("tracker_app.db")
cursor = connect.cursor()
"""creating 5 tables below """
cursor.execute(
    """
               CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                category TEXT,
                amount REAL,
                date TEXT,
                FOREIGN KEY (category) REFERENCES categories(id) ON DELETE CASCADE)
 """
)

cursor.execute(
    """
               CREATE TABLE IF NOT EXISTS income (
                id INTEGER PRIMARY KEY,
                category TEXT,
                amount REAL,
                date TEXT,
                FOREIGN KEY (category) REFERENCES categories(id) ON DELETE CASCADE) 
"""
)

cursor.execute(
    """
               CREATE TABLE IF NOT EXISTS budget (
                id INTEGER PRIMARY KEY,
                category_id INTEGER,
                budget REAL) 
"""
)

cursor.execute(
    """
               CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY,
                goal TEXT,
                goal_amount REAL,
                current_progress REAL)
"""
)

connect.commit()


def adding_expense():
    """This function adds expenses to the expenses table"""
    with sqlite3.connect("tracker_app.db") as connect:
        cursor = connect.cursor()
        expense_category = input("Enter the expense category ")
        expense_amount = float(input("Enter the expense amount "))
        expense_date = input("Enter the date in this format (????-??-??) ")
        cursor.execute(
            """INSERT INTO expenses (category, amount, date) VALUES (?,?,?)""",
            (expense_category, expense_amount, expense_date),
        )
        connect.commit()
        print("Expense added")


def view_expense():
    """This functions allows user to view the expenses from the exepnses table"""
    with sqlite3.connect("tracker_app.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM expenses""")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(
                f"ID: {expense[0]}",
                f"Category: {expense[1]}",
                f"Amount: {expense[2]}",
                f"Date: {expense[3]}",
            )


def view_expense_category():
    """This function allows the user to view the expense category choosen from the expenses table"""
    with sqlite3.connect("tracker_app.db") as connect:
        cursor = connect.cursor()
        category = input("Please enter category to view the expenses ")
        cursor.execute("""SELECT * FROM expenses WHERE category = ?""", (category,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(
                f"ID: {expense[0]}",
                f"Category: {expense[1]}",
                f"Amount: {expense[2]}",
                f"Date: {expense[3]}",
            )


def add_income():
    """This function adds income to the income table"""
    with sqlite3.connect("tracker_app.db") as connect:
        cursor = connect.cursor()
        income_category = input("Enter the income category ")
        income_amount = float(input("Enter the income amount"))
        income_date = input("Enter the date in this format (????-??-??) ")
        cursor.execute(
            """INSERT INTO income (category, amount, date) VALUES (?,?,?)""",
            (income_category, income_amount, income_date),
        )
        connect.commit()
        print("Income added")


def view_income():
    """This function allows user to view income from the income table"""
    with sqlite3.connect("tracker_app.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM income""")
        income = cursor.fetchall()
        for data in income:
            print(data)


def view_income_category():
    """This function allows user to view the income catgory choosen from the income table"""
    with sqlite3.connect("tracker_app.db") as connect:
        cursor = connect.cursor()
        category = input("Please enter the category to view income ")
        cursor.execute("""SELECT * FROM income WHERE category = ?""", (category,))
        income = cursor.fetchall()
        for data in income:
            print(data)


def set_budget():
    """This function allows user to insert a budget in the budget table"""
    with sqlite3.connect("tracker_app.db") as connect:
        cursor = connect.cursor()
        category_id = int(input("Please enter the category ID to set the budget "))
        budget = float(input("Please enter the budget amount for category: "))
        cursor.execute(
            """INSERT INTO budget (category_id, budget) VALUES (?,?)""",
            (category_id, budget),
        )
        connect.commit()
        print(f"The budget was set to {budget}")


def view_budget():
    """This function allows user to view the budget from the budget table"""
    with sqlite3.connect("tracker_app.db") as connect:
        cursor = connect.cursor()
        category_id = int(input("Please enter the category ID to view the budget "))
        cursor.execute(
            """SELECT budget FROM budget WHERE category_id=?""", (category_id,)
        )
        budget = cursor.fetchone()
        if budget:
            print(f"The budget for the category {category_id} is : {budget[0]}")
        else:
            print("Sorry there is no budget set for this category chosen")


def set_goals():
    """This function allows the user to set goals and insert it into the goals table"""
    with sqlite3.connect("tracker_app.db") as connect:
        cursor = connect.cursor()
        goal = input("Please enter goal name ")
        goal_amount = float(input("Please enter goal target amount "))
        current_progress = float(input("Please enter current progress "))
        cursor.execute(
            """INSERT INTO goals (goal, goal_amount, current_progress) VALUES (?,?,?)""",
            (goal, goal_amount, current_progress),
        )
        connect.commit()


def view_progress():
    """This function allows user to view progress from the goals table"""

    with sqlite3.connect("tracker_app.db") as connect:

        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM goals""")
        goals = cursor.fetchall()
        for goal in goals:
            print(
                f"Goal: {goal[1]}",
                f"Goal Amount: {goal[2]}",
                f"Current Progress: {goal[3]}",
            )


def show_menu():
    print("\n1. Add expense ")
    print("2. View expenses ")
    print("3. View expenses by category ")
    print("4. Add income ")
    print("5. View income ")
    print("6. View income by category ")
    print("7. Set budget for a category ")
    print("8. View budget for a category ")
    print("9. Set financial goals ")
    print("10.   View progress towards financial goals ")
    print("11.   Quit ")


def main():
    while True:
        show_menu()
        option = input("Choose an option 1-11 ")

        if option == "1":
            adding_expense()
        elif option == "2":
            view_expense()
        elif option == "3":
            view_expense_category()
        elif option == "4":
            add_income()
        elif option == "5":
            view_income()
        elif option == "6":
            view_income_category()
        elif option == "7":
            set_budget()
        elif option == "8":
            view_budget()
        elif option == "9":
            set_goals()
        elif option == "10":
            view_progress()
        elif option == "11":
            print("Exiting the application.........")
            break
        else:
            print(" Choice is invalid, please try again (1-11) ")


if __name__ == "__main__":
    main()

connect.close()
