# Alex Villanueva

#This code's goal is to make setting up an introductory budget simple and straightforward: taking input about the person and their income and stacking it up against their expenses while giving them insight into what percent of their spending falls in each category --- and finally showing plainly a summary of money in, money out.


name = input("What is your name?: ")
hourly_rate = float(input("What is your hourly pay rate?: "))
# the budgeter-to-be enters their total hours per each of four work weeks
week_1 = float(input("Enter hours for Week 1: "))
week_2 = float(input("Enter hours for week 2: "))
week_3 = float(input("Enter hours for week 3: "))
week_4 = float(input("Enter hours for week 4: "))

# here the monthly expenses (i made them all constants due to the fact that the program has no need to reassign them once they are set and also i said hey what the heck i'm blind anyway and my IDE turns named constants bright orange!)
MONTHLY_CAR_PAYMENT = 357.75
RENT = float(input("Enter monthly rent: "))
UTILITIES = float(input("Enter monthly utilities: "))
TRANSPORTATION = float(input("Enter monthly transportation expenses: "))
FOOD = float(input("Enter monthly cost of food: "))

# add up total hours and save the value to total_hours
total_hours = week_1 + week_2 + week_3 + week_4
# total income is total horus multiplied by hourly rate
total_income = total_hours * hourly_rate
# sum up all expenses and money left over
total_expenses = MONTHLY_CAR_PAYMENT + RENT + UTILITIES + TRANSPORTATION + FOOD
money_left_over = total_income - total_expenses

# now to find out what percentage of the total income each category represents
car_percent = (MONTHLY_CAR_PAYMENT / total_expenses) * 100
rent_percent = (RENT / total_expenses) * 100
utilities_percent = (UTILITIES / total_expenses) * 100
transportation_percent = (TRANSPORTATION / total_expenses) * 100
food_percent = (FOOD / total_expenses) * 100

print(f"\nBudget Report for {name}") #get that name on that headline
print("-" * 50) # lil line for cleanliness

# column formatting first column 20 spaces, second and third column 15. the .2f after 15 tells the code to spit the numbers out to the second decimal e.g. 200.00
print(f"{'Item':<20}{'Amount ($)':<15}{'Percent':<20}") # the column titles i made even 

# tally the percents up
print(f"{'Rent':<20}{RENT:<15.2f}{rent_percent:<15.2f}")
print(f"{'Utilities':<20}{UTILITIES:<15.2f}{utilities_percent:<15.2f}")
print(f"{'Transportation':<20}{TRANSPORTATION:<15.2f}{transportation_percent:<15.2f}")
print(f"{'Food':<20}{FOOD:<15.2f}{food_percent:<15.2f}")
print(f"{'Car Payment':<20}{MONTHLY_CAR_PAYMENT:<15.2f}{car_percent:<15.2f}")
print("-" * 50) # another line

# show total income, expenses, and money left after all is said and done
print(f"{'Total Income':<20}{total_income:<15.2f}")
print(f"{'Total Expenses':<20}{total_expenses:<15.2f}")
print(f"{'Money Left Over':<20}{money_left_over:<15.2f}")