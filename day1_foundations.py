# ==========================================
# DAY 1: PYTHON FOUNDATIONS BOOTCAMP
# Author: Benita Oyinkansola Adakeja
# ==========================================

'''
CHALLENGE 1: VARIABLES & LISTS
1. Create a variable called current_book.
2. Create a list called reading_queue containing three other book titles.
3. Add the string "Think again" to the end of the list.
4. Replace the item at index 0 with a completely different title.
5. Create a new variable called next_up that extracts the first two books using slicing.
6. Print both current_book and next_up.
'''
current_book = "The laws of human nature"
reading_queue = ["The mountain is you", "The outliers", "The light we carry"]

reading_queue.append("Think again")
reading_queue[0] = "Atomic habits"
next_up = reading_queue[0:2]

print("--- Lists Output ---")
print(current_book)
print(next_up)


'''
CHALLENGE 2: FOR LOOPS & F-STRINGS
1. Create a variable called my_name and set it to your name.
2. Create a list called future_roles containing "Data Analyst", "Cloud Engineer", and "DevOps Specialist".
3. Write a for loop that goes through your future_roles list.
4. Use an f-string to print "[Your Name] will be a [Role]" for each item.
'''
my_name = "Benita Oyinkansola Adakeja"
future_roles = ["Data Analyst", "Cloud Engineer", "DevOps Specialist"]

print("\n--- Loops Output ---")
for role in future_roles:
      print(f"{my_name} will be a {role}")


'''
CHALLENGE 3: CONDITIONALS (IF/ELIF/ELSE)
1. Create a list called monthly_bill containing 15, 50, 120.
2. Write a for loop to iterate through the bill.
3. If the bill is < 20, print "Normal usage".
4. Elif the bill is < 100, print "Approaching budget limit".
5. Else, print "ALERT: Budget exceeded!".
'''
monthly_bill = [15, 50, 120]

print("\n--- Conditionals Output ---")
for bill in monthly_bill:
       if bill < 20:
           print("Normal Usage")
       elif bill < 100:
           print("Approaching budget limit")
       else:
           print("ALERT: Budget exceeded!")


'''
CHALLENGE 4: DICTIONARIES
1. Create a dictionary called my_profile.
2. Give it three keys: "name", "role", and "favorite_tool".
3. Assign values to those keys.
4. Write a print statement using an f-string to extract and print the values.
'''
my_profile = {
    "name": "Benita Oyinkansola Adakeja",
    "role": "Data Analyst",
    "favorite_tool": "Power BI"
}

print("\n--- Dictionaries Output ---")
print(f"{my_profile['name']} is a {my_profile['role']} who loves using {my_profile['favorite_tool']}")


'''
CHALLENGE 5: LOOPING THROUGH DICTIONARIES
1. Create a dictionary called aws_progress with 3 services and their status.
2. Write a for loop using .items() to go through the dictionary.
3. Print an f-string that says "Service: [Key] | Status: [Value]".
'''
aws_progress = {
    "EC2": "Completed",
    "S3": "In Progress", 
    "Lambda": "Not Started"
}

print("\n--- Dict Loop Output ---")
for key, value in aws_progress.items():
       print(f"Service: {key} | Status: {value}")


'''
CHALLENGE 6: FUNCTIONS & RETURN STATEMENTS
1. Define a function convert_to_megabytes that accepts gigabytes as a parameter.
2. Multiply gigabytes by 1024 and return the value.
3. Call the function with 5, save it to mb_needed, and print the result.
'''
def convert_to_megabytes(gigabytes):
        total = gigabytes * 1024
        return total

print("\n--- Functions Output ---")
mb_needed = convert_to_megabytes(5)
print(f"You will need {mb_needed} MB of S3 storage") 


'''
CHALLENGE 7: ERROR HANDLING (TRY/EXCEPT)
1. Inside a try block, divide 100 / 0.
2. Inside an except ZeroDivisionError block, print an error message.
3. Un-indented at the bottom, print "Program finished successfully."
'''
print("\n--- Try/Except Output ---")
try:
    result = 100 / 0
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")


'''
CHALLENGE 8: CAPSTONE PROJECT - CLOUD BUDGET AUDITOR
1. Create a dictionary monthly_costs with numbers and one string ("Unknown").
2. Define a function audit_budget(costs_dict).
3. Loop through items. Use a try block to check if value < 100 (print under budget, else over budget).
4. Use an except TypeError block to catch the string and print "data is corrupted!".
5. Call the function.
'''
monthly_costs = {
    "EC2": 85,
    "S3": "Unknown",
    "RDS": 120
}

def audit_budget(costs_dict):
        for key, value in costs_dict.items():
                try:
                  if value < 100:
                      print(f"Status: {key} is under budget")
                  else:
                      print(f"ALERT: {key} is over budget!")
                except TypeError:
                      print(f"Error: {key} data is corrupted!")

print("\n--- Capstone Output ---")
audit_budget(monthly_costs)
