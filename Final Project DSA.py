# EveryDay Life - A simple to-do list application in Python
# This program allows users to add, view, mark as complete, and delete tasks from a to-do list.

import os

file_name = "todo_list.txt"                                                         # File to store the tasks
limit_tasks = 10                                                                    # Maximum number of tasks allowed
tasks = []                                                                          # List to store tasks

<<<<<<< HEAD
#ADD TASK Logic(Fajilan, Mark Justin C.)
=======
# Function to view tasks - Displays the current tasks in the to-do list
# Fajilan, Mark Justin
>>>>>>> 66b0c5dc76db4f887f03e126b1084209054ff8cb
def add_task(task):
    if len(tasks) >= limit_tasks:                                                   # Check if the task limit is reached
        print("Task limit reached. Please delete a task before adding a new one.")
        return
    
    task = input("Enter the task: ").strip()                                        # Prompt user to enter a task
    priority = input("Is it urgent or not urgent? (Y/N): ").strip().lower()         # Prompt user to enter task priority
    
    if priority == "y":                                                             # If the task is urgent, add it to the beginning of the list
        with open(file_name, "a") as file:                                          # Open the file in append mode
            file.write(f"[Urgent] {task}\n")                                        # Write the task to the file
        print(f"Task '{task}' added as urgent and saved successfully.")             # Print confirmation message
    elif priority == "n":                                                           # If the task is not urgent, add it to the end of the list
        with open(file_name, "a") as file:                                          # Open the file in append mode
            file.write(f"[Not Urgent] {task}\n")                                    # Write the task to the file
        print(f"Task '{task}' added as not urgent and saved successfully.")         # Print confirmation message                                         
    else:
<<<<<<< HEAD
        print("Invalid input. Please enter 'Y' for urgent or 'N' for not urgent.")  # Print error message
        return
=======
        print("Invalid input. Please enter 'Y' for urgent or 'N' for not urgent.")
        return
    
    print("Task added successfully!")     
    








































































# Main Menu - Function to display the main menu and handle user input
# Fajilan, Mark Justin
def main():
    while True:
        print("Welcome to EveryDay Life - To-Do List Application")
        print("Please choose an option:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Complete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Program terminated. Thank you for using the program!")
            break
        else:
            print("Invalid input. Try again.\n")

if __name__ == "__main__":
    main()
>>>>>>> 66b0c5dc76db4f887f03e126b1084209054ff8cb
