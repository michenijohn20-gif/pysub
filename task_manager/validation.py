from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Invalid title. Please enter a non-empty task title.")
    return True

def validate_task_description(description):
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Invalid description. Please enter a non-empty task description.")
    if len(description) > 500:
        raise ValueError("Invalid description. Please use 500 characters or fewer.")
    return True

def validate_due_date(due_date):
    if not isinstance(due_date, str) or not due_date.strip():
        raise ValueError("Invalid due date. Please enter a date in YYYY-MM-DD format.")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid due date. Please use YYYY-MM-DD format.")

    return True
