#Alex Villanueva

#The following code is designed to calculate property tax increases in three different tax districts: Burlington, Essex, and everywhere else in Vermont. The UI prints out directions, takes in user input, and applies input to tax calculations, giving Resident interacting with program their new tax rate.

import sys

#save state code as global variable, as well as unchanging tax rates
STATE_CODE = "VT"
BURLINGTON_TAX_RATE = 0.055
ESSEX_TAX_RATE = 0.060
OTHER_TAX_RATE = 0.040

# main function display the directions, receives input from the resident, displays their salutation up top, and then prints letter regarding their property taxes
def main():

  #prints instructions from directions() fx above
  directions()
  print()
  #begin input!
  full_name = input("Enter your full name (type 'quit' to exit): ")
  while full_name.lower() != 'quit':
    street_address = input("Enter street address: ")
    town = input("Enter town: ")
    property_value = float(input("Enter property value: "))

    print()
    print()
    print("-" * 50)
    #calls salutation fx and receives value of full_name as an argument
    print_salutations(full_name)
    print()
    print_letter(street_address, town, property_value)

    full_name = input("Enter your full name (type 'quit' to exit): ")

  sys.exit()

#directions function prints instructions for program to residents
def directions():
  print("1. When prompted for your name, please enter in (first last) format\n"
        "use underscore (_) to represent blanks between first and last name")
  print("2. Enter street address (e.g. 150 Main St)")
  print("3. Enter town or city (e.g. Montpelier)")
  print("[Type 'quit' and hit Enter to exit the program]")



def print_salutations(name):

#replaces underscore with spaces, removes whitespace, and extracts last name from name-array to use in salutation
  name_array = name.replace("_", " ").split()
  last_name = name_array[1]

  print(f"Hello Resident {last_name}")
  
#print_letter fx takes in values of user input, declares a variable for the tax rarte increase, cross-checks input against the three tax districts in question, calculates new tax rate and thusly new tax total.
def print_letter(street_address, town, property_value):
  tax_rate_increase = 1.10

  if town == 'Burlington':
    current_rate = BURLINGTON_TAX_RATE 
  elif town == 'Essex':
    current_rate = ESSEX_TAX_RATE
  else:
    current_rate = OTHER_TAX_RATE
    
  new_tax_rate = current_rate * tax_rate_increase
  new_property_tax = new_tax_rate * property_value

# UI output begins
  print(f"Due to increase in maintenance costs, your property at {street_address} in {town}, {STATE_CODE} will be subject to a property tax increase as of January 2026.\n")
  print()
  print(f"{'Your Property Value: ':<30s}${property_value:<15,.2f}")
  print(f"{'Current Tax Rate: ':<30s}{current_rate:.3f}%")
  print(f"{'New Tax Rate: ':<30s}{new_tax_rate:.3f}%")
  print(f"{'New property tax (Jan 2026)':<30s}: ${new_property_tax:,.2f}")




main()