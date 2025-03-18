## Module 7 Assignment

# Points: 100 points

# This program assesses use of value returning functions and recursion.

# This problem studies use of functions in depreciation. Depreciation is a measure of how much an item is devalued over time. For example, a car depreciates each year such that its worth and thus resell value decreases each year.

# Given an item with an initial worth, salvage value (worth at end of its life), and number of years of life, the annual depreciation can be computed using a variety of formulas.

## Straight line depreciation ## devalues the item the same amount for each year of life. The annual depreciation is: (initial worth – salvage value) / life

# Sum of years depreciation devalues the item by varying amounts depending on the year number. The formula for year y is: ((initial worth - salvage) _ (life - year + 1) _ 2) / (life \* (life + 1))

### Input:

The user enters the positive initial worth, salvage value (0..initial worth), positive life in years. Data validation is performed on each input to ensure correct ranges.

## Processing:

Before the report a decorative pattern of ascending stars appears (see sample output).
For each year in the life, the reports displays the depreciation and current worth using both formulas.
Columns are created using f strings with commas and 2 digits of precision on money amounts.
After the report a decorative pattern of descending stars appears (see sample output).

## Functions:

Code should use the following functions. Do not change the function heading and be sure to honor the
comment.

# def main ( ): # the main method should be placed at top of code

# def get_initial_worth ( ): # use data validation and return valid initial worth

# def get_salvage_value (initial): # use data validation and return valid salvage value

# def get_years (): # use data validation and return valid years of life value

# def printup (life): # print life lines of \* with each row ascending number stars

### this function uses iteration (loop)

# def printdown (life): # print life lines of \* with each row descending number stars

# this function uses recursion

# def sln(initial, salvage, life): # return straight line annual depreciation

# def syr(initial, salvage, life, year): # return sum of years depreciation for given year

## Code Specifications:
-Infinite while True: loops are not accepted. 
-Use of break, continue or other jump statements are not
accepted. 
-Use of structures we have not covered, such as lists or dictionaries, is not accepted. -Lack of
function use is not accepted. 
-Global variables are not accepted.
-The main() function is written on top and called appropriately
-The printup function uses iteration to make the display
-The printdown function uses recursion to make the display
-the sln() function is correct for straight line depreciation
-the syr() function is correct for sum of years depreciation