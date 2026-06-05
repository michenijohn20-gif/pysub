from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        print("Invalid title. Please enter a non-empty task title.")
        return False
    return True

def validate_task_description(description):
    if not isinstance(description, str) or not description.strip():
        print("Invalid description. Please enter a non-empty task description.")
        return False
    return True

def validate_due_date(due_date):
    if not isinstance(due_date, str) or not due_date.strip():
        print("Invalid due date. Please enter a date in YYYY-MM-DD format.")
        return False

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid due date. Please use YYYY-MM-DD format.")
        return False

    return True
