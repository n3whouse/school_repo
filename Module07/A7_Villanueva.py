
# Alex Villanueva

# The function of this program is to calculate the depreciation and current worth of a vehicle entered by a user, using two formulas.

import sys

def main():
    """
    The main function orchestrates the program flow. It will call other functions to get user input,
    perform calculations, and display results.
    """
    # The first step is to collect user inputs. We
    initial_worth = get_initial_worth()
    salvage_value = get_salvage_value(initial_worth)
    life_years = get_years()

    # Step 2: Display decorative star pattern
    printup()  # Print ascending stars

    # Step 3: Calculate and display depreciation for each year
    for year in range(1, life_years + 1):
        straight_line_depreciation = sln(initial_worth, salvage_value, life_years)  # Calculate straight-line depreciation
        sum_years_depreciation = syr(initial_worth, salvage_value, life_years, year)  # Calculate sum-of-years depreciation
        current_worth_straight_line = initial_worth - (straight_line_depreciation * year)  # Calculate current worth
        current_worth_sum_years = initial_worth - sum_years_depreciation  # Calculate current worth

        # Display the results
        print(f"Year {year}: Straight Line Depreciation: ${straight_line_depreciation:,.2f}, Current Worth: ${current_worth_straight_line:,.2f}")
        print(f"Year {year}: Sum of Years Depreciation: ${sum_years_depreciation:,.2f}, Current Worth: ${current_worth_sum_years:,.2f}")

    # Step 4: Display decorative star pattern
    printdown()  # Print descending stars

def get_initial_worth():
    # This fx prompts the user for the initial wroth of their car, converts it to a float, and saves the input as (worth). If it is less than zero, it errors that it must be a positive, non-zero number. Otherwise, the worth is returned.
    try:
        worth = float(input("Enter the initial worth of the vehicle: "))
        if worth <= 0:
            raise ValueError("Initial worth must be a positive number and cannot be zero.")
        return worth
    except ValueError as e:
        print(e)

def get_salvage_value(initial):
    # Prompts the user for the salvage value and validates the input and returns a valid salvage value that is between 0 and the initial worth.

    try:
        salvage = float(input("Enter the salvage value of the vehicle: "))
        if salvage < 0 or salvage > initial:
            raise ValueError(f"Salvage value must be between 0 and {initial}.")
        return salvage
    except ValueError as e:
        print(e)


def get_years():
    # Prompts the user for the number of years of life for the vehicle and validates the input and returns a valid positive number of years.
    try:
        years = int(input("Enter the number of years of life for the vehicle: "))
        if years <= 0:
            raise ValueError("Years must be a positive integer.")
        return years
    except ValueError as e:
        print(e)

def printup():
    # This fx loops through the range 1-9 (non inclusive) and prints the amount of stars that correspond to the line it is looping through (e.g. 4 stars on the 4th line). The loop is killed at 9 so it doesn't run a 9th line.
    for i in range(1, 9):
        print('*' * i)  # Print i stars

def printdown(n=8):
    
    if n > 0:
        print('*' * n)
        printdown(n - 1)

# The previous definition of printdown using iteration has been removed.

def sln(initial, salvage, life):
    
    return (initial - salvage) / life

def syr(initial, salvage, life, year):
    """
    Calculates and returns the sum-of-years depreciation for a given year.
    Formula for year y: ((initial worth - salvage) * (life - year + 1) * 2) / (life * (life + 1))
    """
    return ((initial - salvage) * (life - year + 1) * 2) / (life * (life + 1))


main()
