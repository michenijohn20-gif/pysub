# Import functions from task_manager.task_utils package
from task_manager.task_utils import (
    add_task,
    calculate_progress,
    mark_task_as_complete,
    tasks,
    view_pending_tasks,
)

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
                continue

            for index, task in enumerate(tasks, start=1):
                status = "Complete" if task["completed"] else "Pending"
                print(f"{index}. {task['title']} - {status}")

            try:
                task_number = int(input("Enter task number to mark complete: "))
            except ValueError:
                print("Invalid task number.")
                continue

            mark_task_as_complete(task_number - 1)
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            print(calculate_progress())
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
