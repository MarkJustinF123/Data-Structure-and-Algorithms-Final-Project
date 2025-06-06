# EveryDay Life - A simple to-do list application in Python
# This program allows users to add, view, mark as complete, and delete tasks from a to-do list.

import os
import sys

file_name = "todo_list.txt"                                                         # File to store the tasks
limit_tasks = 10                                                                    # Maximum number of tasks allowed


# Function to load tasks from file
# Gonzales, Johann Franz
def load_tasks(filename=file_name):
   global tasks
   try:
      with open(filename, "r") as file:                                             # Opens the file in read mode 
         return [line.strip() for line in file.readlines()]                         # Returns a list containing each line in the file as a list item
   except FileNotFoundError:                                                        # If file or directory does not exist
      with open(filename, "w") as file:                                            # Create the file if it doesn't exist
         pass
      return []

# Function to save tasks to file
# Gonzales, Johann Franz
def save_tasks(tasks, filename=file_name):                                               
   with open(filename, "w") as file:                                                # Opens the file in write mode
      for task in tasks:                                                            
         file.write(f"{task}\n")                                                   # Edits the content of the file

# Function to exit the program
# Gonzales, Johann Franz
def exit_app():
   print("Program Terminated. Thank you for using Everyday Life. ") 
   sys.exit()                                                                                 # Exits the program

# Function to add a task - Adds a new task to the to-do list
# Fajilan, Mark Justin
def add_task():
    if len(tasks) >= limit_tasks:                                                   # Check if the task limit is reached
        print("Task limit reached. Please delete a task before adding a new one.")
        return
    
    task = input("Enter the task: ").strip()                                        # Prompt user to enter a task
    priority = input("Is it urgent or not urgent? (Y/N): ").strip().lower()         # Prompt user to enter task priority
    
    if priority == "y":                                                             # If the task is urgent, add it to the beginning of the list
        formatted_task = f"[Urgent] {task}"
        tasks.insert(0, formatted_task) 
    elif priority == "n":                                                           # If the task is not urgent, add it to the end of the list
        formatted_task = f"[Not Urgent] {task}"
        tasks.append(formatted_task)                                           
    else:
        print("Invalid input. Please enter 'Y' for urgent or 'N' for not urgent.")
        return
    
    print("Task added successfully!")    
    save_tasks(tasks)                                                               # Save the updated task list to the file 

# Function to display tasks - Displays the current tasks in the to-do list
def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()

    
# Function to delete a task - Removes a task from the to-do list
# Kendric Justine D. Faz
def delete_task():
    display_tasks()                                                                                    # Display current tasks
    if not tasks:                                                                                      # No tasks to delete
        return                                                                                         # Skip to next iteration
    try:
        idx = int(input("Enter the task number to delete: ")) - 1                                      # Get user input
        if 0 <= idx < len(tasks):                                                                      # Check if the index is valid
            removed = tasks.pop(idx)                                                                   # Remove the task
            save_tasks(tasks)                                                                          # Save the updated task list
            print(f"Task Deleted Successfully! ({removed})")                                           # Print success message
        else:
            print("Invalid Task Number")                                                               # Invalid index
    except ValueError:
        print("Invalid input. Please enter a valid task number.")                                      # Handle non-integer input

# Complete Task - Marks a task as complete
# Kendric Justine D. Faz
def complete_task():
    display_tasks()                                                                                    # Show current tasks
    if not tasks:
        return
    try:
        idx = int(input("Enter the task number to mark as complete: ")) - 1                            # Get user input              
        if 0 <= idx < len(tasks):
            if "[Done]" in tasks[idx]:
                print("This task is already marked as complete.")
            else:
                tasks[idx] = f"{tasks[idx]} [Done]"                                                    # Mark task as done
                save_tasks(tasks)
                print(f"Task marked as complete: {tasks[idx]}")
        else:
            print("Invalid Task Number")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


# Main Menu - Function to display the main menu and handle user input
# Fajilan, Mark Justin
def main():
    global tasks
    tasks = load_tasks()                                                                               # Load tasks from file
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
             display_tasks()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            exit_app()
            break
        else:
            print("Invalid input. Try again.\n")

if __name__ == "__main__":
    main()


# EveryDay Life - A simple to-do list application in Python
# The program is a simple to-do list application that allows users to manage their tasks.
# Users can add, delete, view, and mark tasks as complete. The tasks are stored in a text file.
# The program is designed to be user-friendly and provides feedback for each action taken.
# The program is structured with functions for each task, making it easy to maintain and extend.
# The program is designed to be run in a terminal or command prompt.
# The program is a simple to-do list application that allows users to manage their tasks.
# Users can add, delete, view, and mark tasks as complete. The tasks are stored in a text file.
# The program is designed to be user-friendly and provides feedback for each action taken.
# The program is structured with functions for each task, making it easy to maintain and extend.
# The program is designed to be run in a terminal or command prompt.
# The program is a simple to-do list application that allows users to manage their tasks.
# Users can add, delete, view, and mark tasks as complete. The tasks are stored in a text file.

# Members:
# Fajilan, Mark Justin
# Gonzales, Johann Franz
# Kendric Justine D. Faz