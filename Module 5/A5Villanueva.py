# Alex Villanueva

## This program tallies a sample population of employees between 1 and 10. It then asks for their name and converts it to an employee code (first and last initials). It then tallies up hours worked and distinguishes between regular and overtime pay based on if the employee worked more or less than 40 hours. After calculating fed and state taxes, the program outputs a neat wage breakdown per employee. The program uses several nested loops to iterate through the employees and their hours worked to display their information.

## Constants
FEDERAL_TAX_RATE = 0.22
HOURLY_RATE = 18.25

#
number_of_employees = int(input("Enter the number of employees [1-10] (q to quit): "))

while number_of_employees != 'q':
  if number_of_employees < 1 or number_of_employees > 10:
    print("Invalid number of employees. Please enter a number between 1 and 10.")
  else:
    ## this is where we begin the tracking the OT
    overtime_counter = 0
    total_overtime_pay = 0.0 # decimal to the tenth to make sure it's a float

    for r in range (number_of_employees):
      # here i thought it was good practice to distinguish the nested loop running down the list of employees by changing the language a bit to show multiple entries
    
      if r == 0:
        first_and_last = input("Enter the first employee name (Last, First): ") # for the first employee, ask this
      else:
        first_and_last = input("Please enter the next employee's name (Last, First): ") # for every employee after, ask it like this
      while ", " not in first_and_last:
        first_and_last = input("Invalid format. Please enter a name in (Last, First) format: ")

      # here we validate each employee's entered hours
      total_hours = float(input("Enter the total hours employee worked this pay period: "))
      while total_hours < 1 or total_hours > 60:
        total_hours = float(input("Invalid hours. Please enter a number between 1 and 60: "))
      
      # here we validate the number of dependents each employee has
      dependents = int(input("Enter the number of dependents employee has: "))
      while dependents < 0:
        dependents = int(input("Invalid number of dependents. Please enter a positive number: "))

      # here we separate first and last by splitting at the comma and space which make it an array. the first element is the last_name, so the first element of the array [0] is the last_name. The second (after the comma) element of the array [1] is the first_name. employee code is the first letter of first and last, respectively
      last_name = first_and_last.split(", ")[0]
      first_name = first_and_last.split(", ")[1]
      employee_code = first_name[0] + last_name[0]

      #initiate difference in wages
      regular_wages = 0.0
      overtime_wages = 0.0

      if total_hours <= 40:
        regular_wages = total_hours * HOURLY_RATE #no overtime :(
      else:
        regular_wages = 40 * HOURLY_RATE  # First 40 hours at regular rate
        overtime_wages = (total_hours - 40) * HOURLY_RATE * 1.5  # Hours over 40 at overtime rate
        overtime_counter += 1 # that's one more employee making OT
        total_overtime_pay += overtime_wages # Add the overtime wages to total

      #the tax man's comin'
      gross_wages = regular_wages + overtime_wages
      fed_tax = FEDERAL_TAX_RATE * (gross_wages - dependents * 24.32)
      state_tax = 0.04 * gross_wages
      total_taxes = fed_tax + state_tax # just to consolidate/improve readability

      # gross to NET
      net_wages = gross_wages - total_taxes

      print()
      print(f"{'Employee':<15}{'Regular':<15}{'Overtime':<15}{'Federal Tax':<15}{'State Tax':<15}{'Net Wages'}") # the first column
      print ("-" * 75) # for some clean partition
      print(f"{employee_code:<15}{regular_wages:<15.2f}{overtime_wages:<15.2f}{fed_tax:<15.2f}{state_tax:<15.2f}{net_wages:<15.2f}") #2nd column with data
      print()
      print("-" * 75)
      print()
    
    print(f"Number of employees awarded overtime: {overtime_counter}")
    print(f"Total overtime pay: ${total_overtime_pay:.2f}")
    print()

  keep_going = input("Keep going [y/n]?: ")

# added this logic so that the user is prompted as to whether or not they'd like to keep going. the code fires after every employee out of the n employees has been iterated through and total overtime pay and number of employees awarded overtime is calculated and displayed. If 'n', prints Program Finished'. If 'y', ends loop and returns to original prompt.
  while keep_going != "y":
    end_command = input("Program finished.")
    
  number_of_employees = int(input("Enter the number of employees [1-10] (q to quit): "))
