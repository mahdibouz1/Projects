
import datetime
import os
TASK_FILE_ = "tasks.txt"
USER_FILE_ = "user.txt"

def loades_users_from_file():
    '''This loads the list of usernames and passwords from file'''
    users = {}
    if os.path.exists(USER_FILE_):
        with open(USER_FILE_,"r") as file:
            for line in file:
                username,password = line.strip().split(', ')
                users[username] = password
            return users


def validation():
    '''This function validates the username and passwords given'''
    users = loades_users_from_file()
    while True:
        username1 = input('Please enter a username')
        password1 = input('Please enter a password')
        if username1 in users and users[username1] == password1:
            print('Successfully logged in')
            return username1
        else:
            print('Please try again, the password or username is invalid')


def register_user(username1):           
    '''This is an admin only register new user'''
    if username1 != "admin":
        print('Sorry, only an admin can register new users')
        return
    users = loades_users_from_file()
    new_username1 = input('Please enter a new username')
    if new_username1 in users:
        print('Sorry this username already exists, please try again')
        return
    new_password1 = input('Please enter a new password')
    new_password2 = input('Please confirm this new password')
    if new_password1 == new_password2:
        with open(USER_FILE_,"a") as file:
            file.write(f"\n{new_username1}, {new_password1}")
        print('The user has been registered successfully')
    else:
        print('Please try again, the passwords do not match')


def add_task():
    ''''This function adds a new task to the file tasks.txt'''
    assigned_user = input('Please enter the username of whom this task is assigned to')
    title_of_task = input('Please enter the title of the task')
    description_of_task = input('Please enter the description of the task')
    due_date_of_task = input('Please enter the due date of the task in this format (YYYY-MM-DD)')
    assigned_date = datetime.date.today().strftime('%Y-%m-%d')
    completed = 'No'
    with open(TASK_FILE_,"a") as file:
        file.write(f"\n{assigned_user},"
        f" {title_of_task}, "
        f" {description_of_task}," 
        f" {assigned_date}," 
        f" {due_date_of_task}," 
        f" {completed}")
    print('The task has been added')


def view_all_tasks():
    '''This function displays all the tasks from the tasks.txt file'''
    if not os.path.exists(TASK_FILE_):
        print('There are no tasks available to view')
        return
    with open(TASK_FILE_,"r") as file:
        for line in file:
            assigned_user, title_of_task, description_of_task,  \
            assigned_date, due_date_of_task, completed = line.strip().split(", ")
            print(
                f"Task: {title_of_task}\n",
                f"Assigned to: {assigned_user}\n",
                f"Description: {description_of_task}\n",
                f"Assigned Date: {assigned_date}\n",
                f"Due Date: {due_date_of_task}\n",
                f"Completed: {completed}\n---\n"
            )


def view_my_tasks(username1):
    '''This function displays the tasks which are assigned to the logged in user'''
    if not os.path.exists(TASK_FILE_):
        print('There are no tasks available to view')
        return
    with open(TASK_FILE_,"r") as file:
        for line in file:
            assigned_user, title_of_task, description_of_task,\
            assigned_date, due_date_of_task, completed = line.strip().split(", ")
            if assigned_user == username1:
                print(f"Task: {title_of_task}\n"
                f"Description: {description_of_task}\n"
                f"Assigned Date: {assigned_date}\n"
                f"Due Date: {due_date_of_task}\n"
                f"Completed: {completed}\n---")


def display_statistics(username1):
    '''This is an admin only statistic option which displays the total number of users and tasks'''
    if username1 != "admin":
        print('Sorry only admin can view statistics')
        return
    user_number = len(loades_users_from_file())
    task_number = sum(1 for _ in open(TASK_FILE_)) if os.path.exists(TASK_FILE_) else 0
    print("\nStatistics:")
    print(f'The total amount of users: {user_number}')
    print(f'The total amount of tasks: {task_number}')


def main():
    username1 = validation()
    while True:
        print("\nMenu: ")
        if username1 == "admin":
            print("r - Register user")
            print("s- statistic")
            print("a - add task")
            print("va - view all tasks")
            print("vm - view my tasks")
            print("e - exit")
            decision = input("Enter your choice:").lower()
        else:
            print("a - add task")
            print("va - view all tasks")
            print("vm - view my tasks")
            print("e - exit")
            decision = input("Enter your choice:").lower()
        if decision == "r" and username1 == "admin":
            register_user(username1)
        elif decision == "a":
            add_task()
        elif decision == "va":
            view_all_tasks()
        elif decision =="vm":
            view_my_tasks(username1)
        elif decision == "s" and username1 == "admin":
            display_statistics(username1)
        elif decision == "e":
            print('Exiting the program')
            break
        else:
            print('Please try again, invalid input')
            
if __name__ == "__main__":
    main()
    
