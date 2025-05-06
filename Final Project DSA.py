# EveryDay Life - A simple to-do list application in Python
# This program allows users to add, view, mark as complete, and delete tasks from a to-do list.

import os

file_name = "todo_list.txt"                                                         # File to store the tasks
limit_tasks = 10                                                                    # Maximum number of tasks allowed
tasks = []                                                                          # List to store tasks

def add_task(task):
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
    
if __name__ == "__main__":
    add_task(tasks)  #  This will only run the Add Task function
