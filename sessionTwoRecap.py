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