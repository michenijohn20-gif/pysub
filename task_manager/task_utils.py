# Import validation functions
from task_manager.validation import (
    validate_due_date,
    validate_task_description,
    validate_task_title,
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not (
        validate_task_title(title)
        and validate_task_description(description)
        and validate_due_date(due_date)
    ):
        print("Task was not added.")
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")
    return True

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not tasks:
        print("No tasks available.")
        return False

    if not isinstance(index, int) or index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return False

    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]

    if not pending_tasks:
        print("No pending tasks.")
        return []

    print("Pending Tasks:")
    for index, task in enumerate(pending_tasks, start=1):
        print(f"{index}. {task['title']} - Due: {task['due_date']}")
        print(f"   Description: {task['description']}")

    return pending_tasks

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        progress = 0
    else:
        completed_tasks = sum(1 for task in tasks if task["completed"])
        progress = (completed_tasks / len(tasks)) * 100

    print(f"Progress: {progress:.2f}%")
    return progress
