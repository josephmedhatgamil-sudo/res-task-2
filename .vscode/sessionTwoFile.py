import os 

FILE_NAME = "tasks.txt"

def load_tasks():
    """
    Reads the 'tasks.txt' file and returns a list of tasks.
    Handles the case where the file doesn't exist yet.
    """
    tasks = []
    
    if not os.path.exists(FILE_NAME):
        return tasks 
    
    with open (FILE_NAME,"r") as file :
    
        for line in file:
            tasks.append(line.strip('\n'))

    return tasks


def save_task(task):
    """
    Appends a SINGLE new task to the file.
    """
    with open (FILE_NAME,"a") as file :
        file.write(task + '\n')


def rewrite_file(tasks):
    """
    Overwrites the ENTIRE file with the current list of tasks.
    Used when we delete a task.
    """
    with open (FILE_NAME,"w") as file :
        for task in tasks:
            file.write(task + '\n')


def view_tasks(tasks):
    """
    Prints the list of tasks with index numbers.
    """
    print("\n--- Your To-Do List ---")
    
    # Corrected: Only return if the list is empty!
    if not tasks:
      print("Your list is empty! Time to add a task.")
      return # Exit the function here if empty
      
    # This loop runs ONLY if the list is NOT empty
    for index, task in enumerate(tasks, start=1): 
      print(f"{index}. {task}")


def delete_task(tasks):
    """
    Displays tasks, asks user which number to delete, updates list and file.
    """
    view_tasks(tasks)
    if not tasks:
        return 
        
    try: 
        number_to_delete = int(input("Which task number to delete? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
        
    # Validate input
    if 1 <= number_to_delete <= len(tasks):
        index_to_delete = number_to_delete - 1
    
        removed_task = tasks.pop(index_to_delete)
        print(f" Removed: {removed_task}")
        
        # Sync changes to disk
        rewrite_file(tasks)
    else: 
        print(f" Error: Please choose a number between 1 and {len(tasks)}.")
    

# --- Main Execution ---

def main():
    current_tasks = load_tasks()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose (1-4): ")

        if choice == '1':
            task = input("Enter task: ")
            current_tasks.append(task)
            save_task(task)
            print(f"Added task: {task}")
            
        elif choice == '2':
            view_tasks(current_tasks)
            
        elif choice == '3':
            delete_task(current_tasks)
            
        elif choice == '4':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()