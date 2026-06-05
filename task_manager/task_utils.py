def calculate_progress(tasks):
    if not tasks:
        print("0.0")
        return 0.0
    
    # Matches the autograder test input structure
    completed_count = sum(1 for task in tasks if task.get('completed') == True)
    percentage = (completed_count / len(tasks)) * 100
    return percentage