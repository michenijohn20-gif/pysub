task_directory = {}
task_id_counter = 1

def add_task():
    global task_id_counter
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    
    task_directory[task_id_counter] = {
        'title': title,
        'description': description,
        'status': 'pending'
    }
    print(f"Task added with ID: {task_id_counter}")
    task_id_counter += 1

def view_pending_tasks():
    print("\n--- Pending Tasks ---")
    found = False
    for task_id, details in task_directory.items():
        if details['status'] == 'pending':
            print(f"ID: {task_id} | Title: {details['title']} | Description: {details['description']}")
            found = True
    if not found:
        print("No pending tasks.")

def mark_task_complete():
    task_id = int(input("Enter the ID of the task you completed: "))
    if task_id in task_directory:
        task_directory[task_id]['status'] = 'complete'
        print("Task marked as complete.")
    else:
        print("Task ID not found.")

def track_progress():
    total = len(task_directory)
    if total == 0:
        print("No tasks to track.")
        return
    completed = sum(1 for t in task_directory.values() if t['status'] == 'complete')
    percentage = (completed / total) * 100
    print(f"Progress: {completed}/{total} tasks completed ({percentage:.1f}%)")

def main():
    while True:
        print("\n1. Add Task | 2. View Pending | 3. Complete Task | 4. Progress | 5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_pending_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            track_progress()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()