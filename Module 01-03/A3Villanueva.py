# Alex Villanueva

# The goal of this code is to create a program to produce a customer bill. The program will categorize the bill into three types of meals + gratuity. It will also give a breakdown of the room required for the size of the party and applicable taxes -- as well as sum up the grand total

import sys

# Prices of each meal, gratuity, and state tax as constants
BEEF_MEAL_PRICE = 15.95
CHICKEN_MEAL_PRICE = 13.95
VEGAN_MEAL_COST = 10.95
GRATUITY_RATE = 0.18
STATE_TAX_RATE = 0.06


# Room seats and rental fees as constants

ROOM1_SEATS = 200
ROOM1_RENTAL = 250
ROOM2_SEATS = 150
ROOM2_RENTAL = 200
ROOM3_SEATS = 100
ROOM3_RENTAL = 75
ROOM4_SEATS = 30
ROOM4_RENTAL = 50


# Now that all the constants have been named, the number of beef, chicken and vegan meals is read from the keyboard and saved as their respective variables

beef_meals = int(input("Enter the number of beef meals: "))
chicken_meals = int(input("Enter the number of chicken meals: "))
vegan_meals = int(input("Enter the number of vegan meals: "))

total_meals = beef_meals + chicken_meals + vegan_meals

# error handling: if any meals < 0, error. if total meals exceed 200, error and exit. 

if beef_meals < 0 or chicken_meals < 0 or vegan_meals < 0:
  print("Error: Invalid Data")
  sys.exit()


if total_meals > 200:
  print("There is no room large enough")
  sys.exit()

# if-elif-else statement to calculate the smallest size room that will accommodate the party and saving the room price, tax, and total cost as variables to maintain readability and the flexibility of the code 

if total_meals <= ROOM4_SEATS:
  room_price = ROOM4_RENTAL
  room_tax = room_price * STATE_TAX_RATE
  room_cost = room_price + room_tax
  rented_room = 4
elif total_meals <= ROOM3_SEATS:
  room_price = ROOM3_RENTAL
  room_tax = room_price * STATE_TAX_RATE
  room_cost = room_price + room_tax
  rented_room = 3
elif total_meals <= ROOM2_SEATS:
  room_price = ROOM2_RENTAL
  room_tax = room_price * STATE_TAX_RATE
  room_cost = room_price + room_tax
  rented_room = 2
else:
  room_price = ROOM1_RENTAL
  room_tax = room_price * STATE_TAX_RATE
  room_cost = room_price + room_tax
  rented_room = 1

total_beef_meal_cost = beef_meals * BEEF_MEAL_PRICE
total_chicken_meal_cost = chicken_meals * CHICKEN_MEAL_PRICE
total_vegan_meal_cost = vegan_meals * VEGAN_MEAL_COST

meal_cost = total_beef_meal_cost + total_chicken_meal_cost + total_vegan_meal_cost

gratuity = meal_cost * GRATUITY_RATE
total_food_cost = meal_cost + gratuity
total_cost = total_food_cost + room_cost

print()
print("Catering report by Alex Villanueva")
print()
print(f"{'Number of guests':<30s}{total_meals}")
print()


# this series of if statements create conditionals to tally up how much of each meal was ordered by the current party. this is displayed when the code runs, unless the number is zero. if it is zero, the total cost of meals simply does not display. in the case of a negative number being entered, the above error handling will catch it and print an error message at the end of input.
if beef_meals > 0:
  print(f"{'Beef meals':<30s}{beef_meals}")
  print(f"{'Total Cost of Beef Meals':<30s}${total_beef_meal_cost:.2f}")
  print()

if chicken_meals > 0:
  print(f"{'Chicken meals':<30s}{chicken_meals}")
  print(f"{'Total Cost of Chicken Meals':<30s}${total_chicken_meal_cost:.2f}")
  print()

if vegan_meals > 0:
  print(f"{'Vegan meals':<30s}{vegan_meals}")
  print(f"{'Total Cost of Vegan Meals':<30s}${total_vegan_meal_cost:.2f}")
  print()

# the series of print statements below display to the customer a run down of the gratuities and costs of the food and room -- finally displaying the grand total
print()
print(f"{'Gratuity':<30s}${gratuity:.2f}")
print(f"{'Total meal cost':<30s}${total_food_cost:.2f}")
print()

print(f"{'Room Subtotal':<30s}${room_price}")
print(f"{'Room Tax':<30s}${room_tax:.2f}")
print()
print(f"{'Room Total':<30s}${room_cost:.2f}")
print()
print(f"{'Total cost':<30s}${total_cost:.2f}")
print()
