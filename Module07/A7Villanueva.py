# Alex Villanueva

# The function of this program is to calculate the depreciation and current worth of a vehicle entered by a user, using two formulas.

# The main function is written at the top of the program, in order to encapsulate the input functions, do the calculations, and print the outputs within. This way, the only fx that needs to be called at the bottom is main().
def main():
    # The first thing the main fx does is collect user inputs via the pertinent functions, written below main().
    initial_worth = get_initial_worth()
    ## I pass the initial worth into the salvage value function in order to use it for error handling (see get_salvage_value fx)
    salvage_value = get_salvage_value(initial_worth)
    life_years = get_years()

    # Next, we print the ascending stars and follow it with the header.
    printup()
    print(f"{'Year':<10}{'SLN Depreciation':<20}{'SLN Worth':<20}{'SYR Depreciation':<20}{'SYR Worth':<20}")
    print("-" * 50) #lil divider to make it look nice

    # Here we loop through every year in the range of year 1 to the 'life_years' input (+ 1 so it is inclusive of entered year) and calculates the SLN, SYR, and their respective worths.
    for year in range(1, life_years + 1):
        straight_line_depreciation = sln(initial_worth, salvage_value, life_years)
        sum_years_depreciation = syr(initial_worth, salvage_value, life_years, year)
        current_worth_straight_line = initial_worth - (straight_line_depreciation * year)
        current_worth_sum_years = initial_worth - sum_years_depreciation

        ## it then prints them in the same format as the header so everything is aligned
        print(f"{year:<10}{straight_line_depreciation:<20.2f}{current_worth_straight_line:<20.2f}{sum_years_depreciation:<20.2f}{current_worth_sum_years:<20.2f}")
    ## and then it prints the trailing stars to finish off the program printing.
    printdown()

# This fx gets the initial worth by setting worth to a fx scoped variable and the sentinel to valid_input being false. While valid_input remains false, the function prompts. When the user inputs 0 or a negative number, it errors. Otherwise, it sets valid_input to true, ending the loop, returning worth, and moving onto the next input fx.
def get_initial_worth():
    valid_input = False
    worth = 0.0
    while not valid_input:
        try:
            worth = float(input("Enter the initial worth of the vehicle: "))
            if worth <= 0:
                print("Initial worth must be a positive number.")
            else:
                valid_input = True
        except ValueError:
            print("Please enter a valid number for the initial worth.")
    return worth

def get_salvage_value(worth):
    # Prompts the user for the salvage value and validates the input.
    valid_input = False
    salvage = 0.0
    while not valid_input:
        try:
            salvage = float(input("Enter the salvage value of the vehicle: "))
            if salvage < 0:
                print("Salvage value must be a non-negative number.")
            elif salvage > worth:
                print("Salvage value must not be greater than the initial worth.")
            else:
                valid_input = True
        except ValueError:
            print("Please enter a valid number for the salvage value.")
    return salvage

def get_years():
    # Prompts the user for the number of years of life for the vehicle and validates the input.
    valid_input = False
    years = 0
    while not valid_input:
        try:
            years = int(input("Enter the number of years of life for the vehicle: "))
            if years <= 0:
                print("Years must be a positive integer.")
            else:
                valid_input = True
        except ValueError:
            print("Please enter a valid number of years.")
    return years

def printup():
    # This function prints an ascending star pattern.
    for i in range(1, 9):
        print('*' * i)  # Print i stars

def printdown(n=8):
    # This function prints a descending star pattern using recursion.
    if n > 0:
        print('*' * n)
        printdown(n - 1)

def sln(initial, salvage, life):
    return (initial - salvage) / life

def syr(initial, salvage, life, year):
    """
    Calculates and returns the sum-of-years depreciation for a given year.
    Formula for year y: ((initial worth - salvage) * (life - year + 1) * 2) / (life * (life + 1))
    """
    return ((initial - salvage) * (life - year + 1) * 2) / (life * (life + 1))

main()