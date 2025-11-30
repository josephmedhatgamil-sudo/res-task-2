# -----------File-------------
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

#--------------Recap----------
def get_grades():
    """
    Asks the user to input grades one by one and returns a list of those grades.
    """
    # TODO: Initialize an empty list to store the grades
    grades = []
    print("\nEnter grades (type 'done' or '-1' to finish):")

    

    while True:
        # TODO: Take input from the user
        grade = input(">> Grade: ")

        
        # TODO: Check if the user wants to stop
        # Check if the input is 'done' or '-1'. If so, break the loop.
        if grade.lower() == 'done' or grade == '-1': 
          break
        try: 
          # TODO: Convert the input to a number (integer or float)
            actgrade = float(grade)
            # TODO: Add the number to your grades list
            grades.append(actgrade)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
            continue

    # TODO: Return the populated list of grades
    # This is crucial so the other function can use this data.
    return grades
    

def analyze_grades(scores_list):
    """
    Analyzes a list of scores to find the average,
    number of passing grades, and number of failing grades.
    """
    # TODO: Check if the list is empty before proceeding
    # (To avoid dividing by zero later!)
    if not scores_list:
        print("\n analysis failed: No grades were entered.")
        return
    
    
    # TODO: Initialize variables (sum, pass_count, fail_count)
    total_sum = 0 
    pass_count = 0
    fail_count = 0
    passing = 60
    # TODO: Loop through scores_list and calculate stats
    for score in scores_list:
        total_sum += score
    
        if score >= passing:
            pass_count += 1
        else:
            fail_count += 1

    # TODO: Calculate Average and Print results
    total_count = len(scores_list)
    avg = total_sum / total_count

    print(" \n----Grade analysis----")
    print(f"Total grades: {total_count}")
    print(f"Average score: {avg}")
    print(f"Passed students: {pass_count}")
    print(f"Failed students: {fail_count}")

# --- Main Execution ---

# TODO: Call the get_grades function and store the result in a variable
all_score=get_grades()

# TODO: Call the analyze_grades function passing the list you just created
analysis=analyze_grades(all_score)