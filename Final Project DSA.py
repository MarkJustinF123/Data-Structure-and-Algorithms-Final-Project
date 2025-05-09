# EveryDay Life - A simple to-do list application in Python
# This program allows users to add, view, mark as complete, and delete tasks from a to-do list.

import os

file_name = "todo_list.txt"                                                         # File to store the tasks
limit_tasks = 10                                                                    # Maximum number of tasks allowed
tasks = []                                                                          # List to store tasks

#ADD TASK Logic(Fajilan, Mark Justin C.)
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
        print("Invalid input. Please enter 'Y' for urgent or 'N' for not urgent.")  # Print error message
        return