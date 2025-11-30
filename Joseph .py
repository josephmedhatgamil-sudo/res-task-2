"""
INSTRUCTIONS:
- Complete each challenge in order (they build on each other!)
- Run your code after each challenge to test it
- Read the hints if you get stuck
- Delete the 'pass' keyword when you start writing your solution
- Have fun! Making mistakes is part of learning
"""

# ═══════════════════════════════════════════════════════════════════
# CHALLENGE 1: Hello, Resonance! (EASY)
# ═══════════════════════════════════════════════════════════════════
"""
Print a welcome message that says:
"Welcome to Resonance Committee!"
Hint: Use the print() function
"""

# Your code here:
print("Welcome to Resonance Committee!")

# ═══════════════════════════════════════════════════════════════════
# CHALLENGE 2: Personal Greeting (EASY)
# ═══════════════════════════════════════════════════════════════════
"""
Create a variable called 'your_name' with your name in it.
Then print: "Hello, [your_name]! Ready to code?"
Hint: Use an f-string like this: f"Hello, {your_name}!"
"""

# Your code here:
your_name="Joseph"
print(f"Hello, {your_name}! Ready to code?")



# ═══════════════════════════════════════════════════════════════════
# CHALLENGE 3: Interactive Introduction (MEDIUM)
# ═══════════════════════════════════════════════════════════════════
"""
Ask the user for their name and their favorite programming language.
Then print: "[name] loves [language]! That's awesome!"
Hint: Use input() to ask questions
Hint: Store each answer in a different variable
"""

# Your code here:
name= input(" what is your name ")
language= input(" what is your favourite language")
print(f"{name} loves {language}! That's awesome!")


# ═══════════════════════════════════════════════════════════════════
# CHALLENGE 4: Committee Member List (MEDIUM)
# ═══════════════════════════════════════════════════════════════════
"""
Create a list called 'members' with at least 5 names.
Print the first member and the last member.
Hint: Lists use square brackets []
Hint: First item is members[0], last item is members[-1]
"""

# Your code here:
members=["Max","Percy","Jason","Justin","Johnny"]
print(members[0])
print(members[-1])


# ═══════════════════════════════════════════════════════════════════
# CHALLENGE 5: Welcome Everyone! (MEDIUM)
# ═══════════════════════════════════════════════════════════════════
"""
Using the 'members' list from Challenge 4, write a for loop that
prints "Welcome to the team, [name]!" for each member.
Hint: for member in members:
Hint: Don't forget to indent the print statement!
"""

# Your code here:
for person in members:
    print(f"Welcome to the team, {person}!")


# ═══════════════════════════════════════════════════════════════════
# CHALLENGE 6: Add New Members (MEDIUM-HARD)
# ═══════════════════════════════════════════════════════════════════
"""
Ask the user if they want to join the committee (yes or no).
If they say "yes", ask for their name and add it to the members list.
Then print the updated list.
Hint: Use input() and an if statement
Hint: Use members.append() to add to the list
Hint: Check if answer == "yes"
"""

# Your code here:
answer=input('Do you want to join the committee (yes or no). ')
if answer == 'yes':
   new_member=input("tell me your name ")
   members.append(new_member)
   print(members)



# ═══════════════════════════════════════════════════════════════════
# CHALLENGE 7: Age Checker Function (HARD)
# ═══════════════════════════════════════════════════════════════════
"""
Create a function called 'check_eligibility' that takes an age as a parameter.
The function should:
- Print "You can join!" if age >= 16
- Print "Sorry, minimum age is 16" if age < 16
Then test your function with different ages.
Hint: def check_eligibility(age):
Hint: Use if/else inside the function
Hint: Call it like this: check_eligibility(18)
"""

# Your code here:
def check_eligibility(age):
    if age >= 16:
        print("You can join!")
    else:
        print("Sorry, minimum age is 16")

check_eligibility(18)
# ═══════════════════════════════════════════════════════════════════
# CHALLENGE 8: Smart Member Counter (HARD)
# ═══════════════════════════════════════════════════════════════════
"""
Write a function called 'count_members' that:
- Takes a list of members as a parameter
- Returns the number of members
- Prints a message based on the count:
  * "Small team" if < 5 members
  * "Medium team" if 5-10 members
  * "Large team" if > 10 members
Hint: Use len() to count items in a list
Hint: Use if/elif/else for multiple conditions
Hint: Don't forget to 'return' the count!
"""

# Your code here:
def count_members(members):
    member_count = len(members)

    if member_count > 10:
        print("Large team")
    elif member_count >= 5:
        print("Medium team")
    else:
        print("Small team")
        
    return member_count
 


# ═══════════════════════════════════════════════════════════════════
# CHALLENGE 9: Login System (VERY HARD)
# ═══════════════════════════════════════════════════════════════════
"""
Create a simple login system that:
1. Has a list of authorized usernames: ["admin", "alice", "bob"]
2. Asks the user for their username
3. Checks if they're in the authorized list
4. If yes: print "Access granted, [username]!"
5. If username is "admin": also print "You have special privileges"
6. If no: print "Access denied"
Hint: Use 'if username in authorized_users'
Hint: You'll need nested if statements (an if inside another if)
"""

# Your code here:
users=["admin", "alice", "bob"]

def check_user(username):
    if username in users:
        print(f"Access granted, {username}!")
        if username=="admin":
           print("You have special privileges")
    else:
        print("Access denied")   

user_id=input('tell me your name user')
check_user(user_id)

# ═══════════════════════════════════════════════════════════════════
# CONGRATULATIONS!
# ═══════════════════════════════════════════════════════════════════
"""
You've completed you first Python exercises!
Next Steps:
1. Try modifying the challenges to do something different
2. Combine multiple challenges into one big program
3. Share your solutions with the team
4. Start building your own project!
Remember: Every expert was once a beginner. Keep coding! 💻✨
"""