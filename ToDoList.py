
tasks = {}

# Function to add a task
def add_task():
    task_id = len(tasks) + 1
    task_name = input("Enter the task: ")
    tasks[task_id] = task_name
    print(f"Task '{task_name}' added with ID {task_id}")

# Function to remove a task
def remove_task():
    task_id = int(input("Enter the task ID to remove: "))
    if task_id in tasks:
        removed_task = tasks.pop(task_id)
        print(f"Task '{removed_task}' removed successfully")
    else:
        print("Task not found")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for task_id, task_name in tasks.items():
            print(f"{task_id}: {task_name}")

# Main program loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
