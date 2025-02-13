import os

# Define the file where tasks will be stored
TASK_FILE = 'tasks.txt'

# Function to read tasks from the file
def read_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

# Function to write tasks to the file
def write_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to display tasks
def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print(f"Task '{task}' added.")

# Function to remove a task by its number
def remove_task(task_number):
    tasks = read_tasks()
    if task_number < 1 or task_number > len(tasks):
        print(f"Error: Task number {task_number} is not valid.")
    else:
        removed_task = tasks.pop(task_number - 1)
        write_tasks(tasks)
        print(f"Task '{removed_task}' removed.")

# Main function to interact with the user
def main():
    while True:
        
        print("\n--------------------------------")
        print("\nTo-Do List Application\n")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit\n")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            view_tasks()
        elif choice == 2:
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == 3:
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == 4:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
